#!/usr/bin/env python3
"""
qadr_cli.py
Main CLI orchestrator (serverless). Loads Python plugins, runs them,
collects results, optionally sends a summary to an AI endpoint for analysis.
"""

import os
import sys
import json
import argparse
import importlib.util
from pathlib import Path
from datetime import datetime
import requests  # required for optional AI calls

ROOT = Path(__file__).resolve().parent
PLUGINS_DIR = ROOT / "plugins"
I18N_DIR = ROOT / "i18n"
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

# Load i18n
def load_locale(lang="en"):
    p = I18N_DIR / f"{lang}.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))

# Simple plugin loader: Python modules exposing `run()` -> dict
def load_plugins():
    plugins = {}
    if not PLUGINS_DIR.exists():
        return plugins
    for f in PLUGINS_DIR.glob("*.py"):
        name = f.stem
        spec = importlib.util.spec_from_file_location(name, str(f))
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            if hasattr(mod, "run") and callable(mod.run):
                plugins[name] = mod
        except Exception as e:
            print(f"[WARN] failed to load plugin {name}: {e}")
    return plugins

def run_plugins(plugins, args):
    results = {}
    for name, mod in plugins.items():
        try:
            res = mod.run(args)
            results[name] = {"status": "ok", "result": res}
        except Exception as e:
            results[name] = {"status": "error", "error": str(e)}
    return results

def summarize_results(results):
    # Basic summarization that can be extended or replaced by AI analysis
    summary = {"timestamp": datetime.utcnow().isoformat()+"Z", "plugins": {}}
    for k,v in results.items():
        summary["plugins"][k] = {
            "status": v.get("status"),
            "keys_found": [] if v.get("status")!="ok" else list(v["result"].get("keys", []))[:5],
            "note": v.get("result", {}).get("note", "")
        }
    return summary

def send_to_ai(api_url, api_key, payload):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    try:
        resp = requests.post(api_url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(prog="qadr-cli")
    parser.add_argument("--lang", default="en", help="locale (en/ar)")
    parser.add_argument("--list-plugins", action="store_true")
    parser.add_argument("--plugin", action="append", help="run specific plugin(s) by name")
    parser.add_argument("--ai", help="AI analysis endpoint URL (optional)")
    parser.add_argument("--ai-key", help="AI API key (optional; better use env GEMINI_API_KEY etc.)")
    parser.add_argument("--out", help="output file (defaults to artifacts/result-<ts>.json)")
    args = parser.parse_args()

    locale = load_locale(args.lang)
    plugins = load_plugins()
    if args.list_plugins:
        print("Available plugins:", ", ".join(plugins.keys() or ["<none>"]))
        sys.exit(0)

    to_run = plugins
    if args.plugin:
        to_run = {k:v for k,v in plugins.items() if k in args.plugin}

    print(locale.get("start", "Starting QADR CLI..."))
    results = run_plugins(to_run, vars(args))
    summary = summarize_results(results)

    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    outpath = Path(args.out) if args.out else ARTIFACTS / f"result-{ts}.json"
    outpath.write_text(json.dumps({"meta": {"locale": args.lang, "ts": ts}, "results": results, "summary": summary}, indent=2), encoding="utf-8")
    print(f"Results written to {outpath}")

    # Optional: send summary to AI for deeper analysis
    ai_url = args.ai or os.getenv("QADR_AI_URL")
    ai_key = args.ai_key or os.getenv("QADR_AI_KEY")
    if ai_url and ai_key:
        print("Sending summary to AI for analysis...")
        ai_resp = send_to_ai(ai_url, ai_key, {"summary": summary, "results_meta": {"plugins": list(results.keys())}})
        ai_out = ARTIFACTS / f"ai-{ts}.json"
        ai_out.write_text(json.dumps(ai_resp, indent=2), encoding="utf-8")
        print(f"AI response saved to {ai_out}")

    print(locale.get("done", "Done."))

if __name__ == "__main__":
    main()!/usr/bin/env bash
# git-optional-commit.sh
# Utility to stage/commit/push with a few convenient flags.
# Usage examples are provided in READ