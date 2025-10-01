# SULTAN-AAA-SYNC
SULTAN-AAA# Hello — SULTAN‑AAA QADR CLI / مرحبًا — واجهة سطر أوامر SULTAN‑AAA QADR

Hello! 👋  
Welcome to **SULTAN‑AAA QADR CLI**, a unified local automation tool to clone, set up, and run `text-generation-webui`, Node.js scripts, Python agents, and optional server processes. The branch runs through AI systems to perform automated analysis and tasks.

مرحبًا! 👋  
أهلاً بك في **SULTAN‑AAA QADR CLI** — أداة محلية موحدة لاستنساخ، إعداد وتشغيل `text-generation-webui`، سكربتات Node.js، وكلاء Python، وخوادم اختيارية. هذا الفرع يعمل عن طريق أنظمة الذكاء الاصطناعي لأداء التحليل والمهام التلقائية (خلفيًّا).

---

## One-line summary / ملخّص سريع
A local, admin‑friendly CLI that handles repo setup, encrypted environment keys, and running background AI agents.  
أداة محلية سهلة للمسؤول تتكفل بإعداد المستودع، تشفير مفاتيح البيئة، وتشغيل وكلاء الذكاء الاصطناعي في الخلفية.

---

## Features — المزايا
- Idempotent clone/update (safe to re-run).  
- Encrypted `.env` handling (`.env.enc`) with admin‑bypass support.  
- Start/stop/status management for Node and Python processes and optional server.  
- Local logs & artifacts; temporary decrypted files are cleaned automatically.  
- Backend AI automation (works via configured AI systems).  

- استنساخ/تحديث آمن قابل للتكرار.  
- تشفير ملف البيئة (`.env.enc`) مع دعم تجاوز إداري (Admin‑bypass).  
- أوامر تشغيل/إيقاف/حالة لعمليات Node و Python وخادم اختياري.  
- سجلات محلية وملفات مؤقتة تُحذف تلقائيًا.  
- تحليلات وآليات تلقائية تعمل عبر أنظمة الذكاء الاصطناعي (خلفيًّا).

---

## Quick Start — البدء السريع (very simple / بسيط جداً)

1. Make the CLI executable / اجعل السكربت قابلاً للتنفيذ:
```bash
chmod +x sultan_setup_cli.sh
