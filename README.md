"Qadr"
👋 أهلاً بك في ملفي الشخصي | Welcome to my Profile
أنا سلطان (SULTAN-AAA)

باحث ومطور ذكاء اصطناعي & خبير أمن سيبراني

AI Researcher @ University of Malaya | Cybersecurity Specialist

ORCID iD

🇸🇦 أبحث عن فرص في جدة	Looking for opportunities in Jeddah 🇸🇦
✍️ نبذة عني | About Me

طالب وباحث في جامعة مالايا (UM)، أجمع بين قوة الذكاء الاصطناعي وعمق الأمن السيبراني. متخصص في تطوير الأنظمة الذكية وتأمينها، مع خبرة واسعة في الاختراق الأخلاقي والدفاع الرقمي. أسعى لتوظيف تقنيات الـ AI لخدمة الحلول الأمنية والمشاريع التقنية المبتكرة في المملكة العربية السعودية.

AI Researcher at University of Malaya. I bridge the gap between AI and Cybersecurity. Specialist in developing intelligent systems and securing them, with expertise in Ethical Hacking and Cyber Defense. My goal is to leverage AI for advanced security solutions.

🚀 المهارات التقنية | Technical Skills

🧠 الذكاء الاصطناعي & البرمجة

     
🛡️ الأمن السيبراني | Cybersecurity

     
🛠 المشاريع الحالية | Projects

Project Qadr: مشروع ريادي يهدف إلى [أضف وصفاً موجزاً لجوهر المشروع، مثلاً: توفير حلول تقنية ذكية].
AI-Driven Security: أبحاث حول دمج خوارزميات تعلم الآلة في كشف التسلل (IDS) وحماية البيانات.
📊 إحصائيات GitHub | Stats

 

📞 تواصل معي | Connect with me[+60-182945341]

ORCID: 0009-0005-6414-2037
الخاص بك]
dxoom18@hmail.com: [إيميلك الرسمي]
مشروع **QADR CLI** أداة موحدة لتحليل البيانات تعمل من **الكونسول** مباشرة.  
تجمع بين:  
‏- 🔍 **OSINT** (جمع وتحليل بيانات من الروابط)  
‏- 📡 **BLE** (اكتشاف أجهزة Bluetooth LE والتواصل معها)  
‏- 🌐 **Tor Proxy** (إخفاء الهوية أثناء الجمع)  
‏- ☁️ **Google Cloud Storage** (رفع النتائج وحفظها آمنًا)  

⚠️ **تنبيه مهم**: الأداة مصممة للاستخدام القانوني والأخلاقي فقط. أي استخدام مسيء يقع على عاتق المستخدم.

---

## 📂 هيكل المشروع

---

## ⚡️ التثبيت والتشغيل

```bash
# استنساخ المشروع
git clone https://github.com/Abdiifahman/SULTAN-AAA-SYNC.git qadr-cli
cd qadr-cli

# تثبيت الأداة
bash setup.sh

# تشغيل الأداة
qadr --ble --osint https://example.com --tor

scanner:
  mode: passive
  timeout: 10
  rate_limit_per_host: 1
  redact_sensitive: true

consent:
  required: true
  disclaimer: "For authorized and legal use only"

logging:
  level: info
  save_to_file: true

name: QADR CLI CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run basic check
        run: python qadr_cli.py --help
storage config "git checkout main git pull origin main" "git checkout -b common" "mkdir -p ai_detection defense_engine models/trained_models integration tests docs src/osint src/ble src/tor_proxy src/storage config
#!/bin/bash  # سكربت bash لإصلاح جميع المشاكل في repo SULTAN-AAA-SYNC، # إنشاء branch common، إضافة الملفات المفقودة لجعل المشروع QADR-AI-Shield كاملاً واحترافياً، # تحديث الهيكل، إضافة CI/CD، LICENSE، Dockerfile، tests، إلخ. # افتراض: أنت في الدليل المحلي للـ repo (git clone https://github.com/Abdiifahman/SULTAN-AAA-SYNC.git) # ستحتاج إلى صلاحيات push إلى origin.  # خطوة 1: التأكد من التحديث من main git checkout main git pull origin main  # خطوة 2: إنشاء branch common للتطوير الكامل git checkout -b common  # خطوة 3: إنشاء الهيكل الكامل لـ QADR-AI-Shield (حل مشكلة النقص في الملفات) mkdir -p ai_detection defense_engine models/trained_models integration tests docs src/osint src/ble src/tor_proxy src/storage config  # إضافة ملفات أساسية (محتوى مبسط/مستوحى من اقتراحات سابقة)  # .gitignore (إذا مفقود، حل مشكلة رفع الملفات غير الضرورية) if [ ! -f .gitignore ]; then   cat <<
/**
 * Qadr CLI - Ultimate Engine Plugin (ngrok-docs Edition)
 * Author: SULTAN-AAA (AI Researcher & Cybersecurity Specialist)
 * Capability: Multi-Language Processing, Dynamic Reordering, & Non-Destructive Cleaning.
 */

const fs = require('fs');
const path = require('path');

const qadrEngine = {
    // 1. القواميس والمعالجات (Multi-Language Parsers)
    parsers: {
        md: (data) => {
            console.log('[Qadr Parser] Cleaning Markdown while preserving Arabic/Emojis...');
            // تنظيف الرموز التحكمية فقط والحفاظ على النصوص العالمية
            let content = data.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F]/g, '').replace(/\r\n/g, '\n');
            
            // توليد فهرس تلقائي (TOC) إذا كان الملف طويلاً وغير محتوي على واحد
            if (!content.includes('## Table of Contents') && content.split('\n').length > 15) {
                const headings = content.match(/^##\s+.+/gm);
                if (headings) {
                    const toc = `## Table of Contents\n${headings.map(h => {
                        const title = h.replace('## ', '');
                        return `* [${title}](#${title.toLowerCase().trim().replace(/\s+/g, '-')})`;
                    }).join('\n')}\n\n`;
                    content = content.replace(/^(#\s+.+\n)/, `$1\n${toc}`);
                }
            }
            return content;
        },
        mdx: (data) => qadrEngine.parsers.md(data),
        
        json: (data, filePath) => {
            try {
                const parsed = JSON.parse(data);
                // ميزة الترتيب الذكي لملف docs.json (حل مشكلة الترتيب)
                if (path.basename(filePath) === 'docs.json' && parsed.navigation) {
                    const priority = ['Start', 'AI Gateway', 'Universal Gateway'];
                    parsed.navigation.sort((a, b) => {
                        const ia = priority.indexOf(a.group || a.title);
                        const ib = priority.indexOf(b.group || b.title);
                        if (ia !== -1 && ib !== -1) return ia - ib;
                        if (ia !== -1) return -1;
                        if (ib !== -1) return 1;
                        return (a.group || a.title || "").localeCompare(b.group || b.title || "");
                    });
                    console.log('[Qadr Reorder] docs.json Navigation structure optimized.');
                }
                return JSON.stringify(parsed, null, 2) + '\n';
            } catch (e) {
                console.warn(`[Qadr JSON] Error in ${filePath}: Invalid JSON syntax.`);
                return data;
            }
        },

        preserve: (data) => data // للغات مثل Go لضمان عدم المساس بالكود البرمجي
    },

    // 2. المحرك الرئيسي (Execution Core)
    execute: function(filePath) {
        try {
            if (!fs.existsSync(filePath)) return;
            
            const ext = path.extname(filePath).toLowerCase().slice(1);
            const originalContent = fs.readFileSync(filePath, 'utf8');
            let processedContent = originalContent;

            console.log(`\n[Qadr Engine] >>> Processing: ${filePath}`);

            // اختيار المعالج المناسب بناءً على اللغة
            if (['md', 'mdx', 'markdown'].includes(ext)) {
                processedContent = this.parsers.md(originalContent);
            } else if (ext === 'json') {
                processedContent = this.parsers.json(originalContent, filePath);
            } else if (['go', 'js', 'py'].includes(ext)) {
                processedContent = this.parsers.preserve(originalContent);
            }

            // الحفظ فقط في حال حدوث تغيير (Optimization)
            if (processedContent !== originalContent) {
                fs.writeFileSync(filePath, processedContent, 'utf8');
                console.log(`[Qadr Engine] ✅ Successfully Updated: ${filePath}`);
            } else {
                console.log(`[Qadr Engine] ℹ️ No changes needed for: ${filePath}`);
            }

        } catch (err) {
            console.error(`[Qadr Engine] ❌ Critical Error on ${filePath}:`, err.message);
        }
    },

    // 3. التشغيل الشامل (Batch Processing)
    runBatch: function(targetFiles) {
        console.log('--- QADR CLI ENGINE START ---');
        targetFiles.forEach(file => this.execute(file));
        console.log('--- QADR CLI ENGINE FINISHED ---');
    }
};

// ملفات الاختبار المستهدفة في ngrok-docs
const filesToProcess = [
    'README.md',
    'docs.json',
    'docs/ai-gateway/overview.mdx'
];

qadrEngine.runBatch(filesToProcess);

module.exports = qadrEngine;
# 1. تحديث وتأمين الهوية البرمجية
git config user.name "SULTAN-AAA"
git config user.email "sultan@qadr-engine.com" # أو إيميلك الرسمي

# 2. حقن بيان حقوق الملكية والشرط التجاري في كل الملفات (Automated Injection)
# هذا الجزء يضمن أن بصمتك موجودة في كل مكان
find . -type f \( -name "*.js" -o -name "*.go" -o -name "*.py" \) -exec sed -i '1i /** © 2026 SULTAN-AAA | Qadr Engine | Commercial Use Requires Profit-Share Agreement **' {} +

# 3. إنشاء/تحديث ملف الترخيص القانوني الصارم
cat << EOF > LICENSE.md
# Qadr Engine Commercial License
© 2026 SULTAN-AAA. All Rights Reserved.

## Commercial Terms:
- Any commercial integration of Qadr Engine or its derivatives is subject to a mandatory royalty fee.
- The Author (SULTAN-AAA) reserves the right to determine the profit-sharing percentage upon revenue generation.
- Unauthorized commercial use will be subject to legal action under IP laws.
EOF

# 4. إضافة كافة التغييرات بما فيها تحسينات ngrok الأخيرة
git add .

# 5. توثيق الرفع برسالة "مستوى المهندسين الكبار"
git commit -m "Final: Deploy Qadr Engine v1.0.0
- Full documentation & CI/CD automation integrated.
- Legal & Commercial protection layers injected.
- Syncing with SULTAN-AAA Ecosystem & ngrok-docs."

# 6. المزامنة النهائية (Syncing to the World)
git push origin main
Qadr-CLI/
├── .github/                # إعدادات الأتمتة والـ Actions
├── sync/                   # ملفات المزامنة (Sync Files)
│   ├── ngrok_config.yml    # إعدادات النفق المشفر
│   ├── sync_notice.txt     # إشعار حقوق الملكية (Copyright Notice)
│   └── .qadr_sync_meta     # بيانات المزامنة الوصفية
├── core/                   # المحرك الأساسي (Qadr Engine)
│   ├── engine.py           # منطق التشغيل الرئيسي
│   └── ppmm_handler.py     # وحدة معالجة الـ PPMM (الجديدة)
├── docs/                   # التوثيق المتقدم
│   ├── api_specs.mdx       # توثيق الـ API بنظام MDX (تفاعلي)
│   └── usage_guide.mdx     # دليل الاستخدام بنظام MDX
├── modules/                # الأدوات السيبرانية المدمجة
│   └── tunnel_manager.py   # مدير اتصالات ngrok
├── scripts/                # سكربتات التشغيل السريع
└── LICENSE                 # ملف الترخيص مع شرط الأرباح المذكور سابقاً
© 2026 Qadr Engine - Developed by SULTAN-AAA.
All Rights Reserved. 
Commercial use of this engine or its sync files is strictly prohibited 
without prior written consent and an agreed-upon royalty fee.