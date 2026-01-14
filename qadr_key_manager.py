#!/usr/bin/env python3
# -*- coding: utf-8 -*بللclass QadrGhost:
    def start(self):
        # 1. إخفاء الهوية
        # 2. تشغيل النفق (ngrok)
        # 3. مسح الآثار فور الخروج
        print("Qadr Engine: Ghost Mode Active... 👻")

QADR Decentralized Key Manager
نظام مفاتيح API لامركزي بالكامل
"""

import os
import base64
import json
import time
import hashlib
import secrets
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class QADRKeyManager:
    """مدير مفاتيح API اللامركزي"""

    def __init__(self, master_key_path="qadr_master.key"):
        self.master_key_path = master_key_path
        self.master_key = self._load_or_create_master()
        self.sub_keys = {}
        self.rotation_interval = 3600  # تدوير كل ساعة
        self.last_rotation = 0

    # -----------------------------
    # 1) Master Key
    # -----------------------------
    def _load_or_create_master(self):
        if os.path.exists(self.master_key_path):
            with open(self.master_key_path, "rb") as f:
                return f.read()
        else:
            mk = get_random_bytes(32)  # AES256
            with open(self.master_key_path, "wb") as f:
                f.write(mk)
            return mk

    # -----------------------------
    # 2) Encryption Helper
    # -----------------------------
    def _encrypt(self, data: bytes):
        cipher = AES.new(self.master_key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def _decrypt(self, encoded: str):
        raw = base64.b64decode(encoded)
        nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
        cipher = AES.new(self.master_key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag)

    # -----------------------------
    # 3) SubKey Generator
    # -----------------------------
    def generate_subkey(self, module_name: str):
        raw_key = secrets.token_hex(32)
        signed = hashlib.sha256((raw_key + module_name).encode()).hexdigest()

        encrypted_key = self._encrypt(raw_key.encode())

        self.sub_keys[module_name] = {
            "raw": encrypted_key,
            "signature": signed,
            "timestamp": time.time(),
        }

        return encrypted_key

    # -----------------------------
    # 4) Validate Key
    # -----------------------------
    def validate_subkey(self, module_name: str, encrypted_key: str):
        if module_name not in self.sub_keys:
            return False

        stored = self.sub_keys[module_name]

        if stored["raw"] != encrypted_key:
            return False

        # expiry
        if time.time() - stored["timestamp"] > self.rotation_interval:
            return False

        try:
            raw = self._decrypt(encrypted_key).decode()
            sig = hashlib.sha256((raw + module_name).encode()).hexdigest()
            return sig == stored["signature"]
        except:
            return False

    # -----------------------------
    # 5) Auto Rotation
    # -----------------------------
    def rotate(self):
        if time.time() - self.last_rotation > self.rotation_interval:
            for module in list(self.sub_keys.keys()):
                self.generate_subkey(module)
            self.last_rotation = time.time()


# نسخة جاهزة للاستخدام
key_manager = QADRKeyManager()

qadr_osint.key
qadr_network.key
qadr_ai.key
qadr_autopentest.key



qadr_master.key
*.token
*.secret
.env

client → QADR Key Manager → DeepSeek API

subkey = key_manager.generate_subkey("ai_module")
print("🔑 استخدم المفتاح:", subkey)

.gitignore

from qadr_key_manager import key_manager



os.chmod(self.master_key_path, 0o600)

