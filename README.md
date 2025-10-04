# SULTAN-AAA-SYNC
SULTAN-AAA
# init_project.sh - Setup QADR CLI repo with all core files
#!/bin/bash
# init_project.sh - Setup QADR CLI repo with all core files

# 1. استنساخ المستودع
git clone https://github.com/Abdiifahman/SULTAN-AAA-SYNC.git qadr-cli
cd qadr-cli || exit 1

# 2. إنشاء الملفات الأساسية
cat > README.md <<'EOF'
# QADR CLI
(نفس النص اللي كتبته لك فوق كامل README.md)
EOF

cat > CONTRIBUTING.md <<'EOF'
(النص الكامل لملف CONTRIBUTING.md)
EOF

cat > CODE_OF_CONDUCT.md <<'EOF'
(النص الكامل لملف CODE_OF_CONDUCT.md)
EOF

cat > LICENSE <<'EOF'
(نص Apache-2.0 License كامل)
EOF

cat > config.yaml <<'EOF'
scanner:
  mode: passive
  timeout: 10
  rate_limit_per_host: 1
  redact_sensitive: true
consent:
  required: true
EOF

cat > qadr_cli.py <<'EOF'
(الكود الكامل اللي رتبناه للـ QADR CLI)
EOF

cat > setup.sh <<'EOF'
#!/bin/bash
echo "[*] Installing dependencies..."
pip install -r requirements.txt
chmod +x qadr_cli.py
sudo ln -sf $(pwd)/qadr_cli.py /usr/local/bin/qadr
echo "[*] Done! Now run: qadr"
EOF

cat > requirements.txt <<'EOF'
requests
rich
bleak
google-cloud-storage
EOF

# 3. حفظ التغييرات على Git
git add .
git commit -m "Initialize QADR CLI with docs, license, and core files"
git push origin main