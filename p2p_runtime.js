// install: npm install libp2p @libp2p/tcp @libp2p/websockets @libp2p/mplex @chainsafe/libp2p-noise @multiformats/multiaddr yaml fs
const { createLibp2p } = require('libp2p');
const { tcp } = require('@libp2p/tcp');
const { webSockets } = require('@libp2p/websockets');
const { mplex } = require('@libp2p/mplex');
const { noise } = require('@chainsafe/libp2p-noise');
const { multiaddr } = require('@multiformats/multiaddr');
const fs = require('fs');
const yaml = require('yaml');  // For parsing AILL YAML

// trustedPeerIds.json contains array of peerIds/public keys you allow
const trusted = JSON.parse(fs.readFileSync('./trustedPeerIds.json', 'utf8'));

// Load AILL doc
const loadDoc = (path) => yaml.parse(fs.readFileSync(path, 'utf8'));

// Simulate step (local, safe — no real egress)
const simulateStep = (step, context, signedPolicy = false) => {
  const sid = step.id;
  const net = step.resources?.network || 'none';
  console.log(`[SIM/P2P] Step: ${sid} | network=${net}`);
  if (net !== 'none' && !signedPolicy) {
    console.log('  - Blocked: No signed policy for egress. Use --allow-signed-egress');
    return { status: 'blocked', step: sid };
  }
  // Mock output (local inference only)
  const outputHash = require('crypto').createHash('sha256').update(sid + JSON.stringify(context)).digest('hex');
  return { status: 'ok', step: sid, output_hash: outputHash };
};

// Build simple DAG from workflow
const buildDag = (workflow) => workflow;  // Linear for demo

// Main P2P node
async function main() {
  const args = process.argv.slice(2);
  const docPath = args.find(arg => arg.startsWith('--doc='))?.split('=')[1];
  const dryRun = args.includes('--dry-run');
  const simulateDomain = args.find(arg => arg.startsWith('--simulate-domain='))?.split('=')[1];
  const allowSignedEgress = args.includes('--allow-signed-egress');

  if (!docPath) {
    console.error('Usage: node p2p_runtime.js --doc aill_example.yaml [--dry-run] [--simulate-domain example.com] [--allow-signed-egress]');
    process.exit(1);
  }

  const doc = loadDoc(docPath);
  const workflow = doc.workflow || [];
  console.log(`Loaded AILL: ${doc.meta?.project_id} v${doc.meta?.version}`);
  console.log('Intent:', doc.intent?.summary);

  const node = await createLibp2p({
    transports: [tcp(), webSockets()],
    streamMuxers: [mplex()],
    connectionEncryption: [noise()],
    // Add peer discovery if needed (e.g., bootstrap list from trusted)
  });

  await node.start();
  console.log('P2P Node started, ID=', node.peerId.toString());

  // P2P Handler for /ai-core/exec (integrated with AILL)
  node.handle('/ai-core/exec/1.0.0', async ({ stream, connection }) => {
    const peerId = connection.remotePeer.toString();
    if (!trusted.includes(peerId)) {
      console.log('Rejecting exec from untrusted peer:', peerId);
      await stream.close();
      return;
    }
    console.log('Accepted exec from trusted peer:', peerId);
    // Read request (e.g., AILL step JSON)
    let request = '';
    for await (const chunk of stream) {
      request += chunk.toString();
    }
    const step = JSON.parse(request);  // Assume step sent as JSON
    const context = { /* from shared state */ };
    const signedPolicy = allowSignedEgress;  // Check signature in prod
    const result = simulateStep(step, context, signedPolicy);
    // Send back signed result
    await stream.write(JSON.stringify(result));
    await stream.close();
  });

  // Local simulation (non-P2P mode)
  if (dryRun || !simulateDomain) {
    const dag = buildDag(workflow);
    let context = { intent_inputs: {}, meta: doc.meta || {} };
    if (simulateDomain) {
      console.log(`*** DOMAIN SIM MODE (MOCK) for: ${simulateDomain} ***`);
      context.simulate_domain = simulateDomain;
    }
    for (const step of dag) {
      console.log('\n---');
      const result = simulateStep(step, context, allowSignedEgress);
      context[step.id] = result;
      if (result.status !== 'ok') {
        console.log(`Step ${step.id} failed. Aborting.`);
        break;
      }
    }
    console.log('\nSimulation complete. Artifacts (mock):');
    for (const [k, v] of Object.entries(context)) {
      if (k !== 'intent_inputs' && k !== 'meta') {
        console.log(` - ${k}: ${v.output_hash}`);
      }
    }
  }

  // Dial trusted peers for discovery (optional)
  for (const peerId of trusted) {
    try {
      await node.dial(multiaddr(`/ip4/127.0.0.1/tcp/0/p2p/${peerId}`));  // Example local multiaddr
    } catch (e) {
      console.log('Failed to dial peer:', peerId, e.message);
    }
  }

  // Keep alive
  process.on('SIGINT', async () => {
    await node.stop();
    process.exit(0);
  });
}

main().catch(console.error);