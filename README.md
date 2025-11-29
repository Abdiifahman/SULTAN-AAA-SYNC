"Qadr"

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