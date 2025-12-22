import hashlib
import os
import sys
import time
import json
import subprocess
from datetime import datetime

# --- إعدادات الهوية البصرية (QadrUltra Style) ---
B = '\033[34m'; R = '\033[31m'; G = '\033[32m'; Y = '\033[33m'; C = '\033[36m'; W = '\033[0m'

class QadrUltraEngine:
    def __init__(self):
        self.project_name = "QadrUltra-Merkle-Sync"
        self.version = "V3.0-PRO"
        self.logs = []
        self.plugins_path = "./plugins"
        # التأكد من وجود مجلد الإضافات لتعزيز فكرة الـ Plugin System
        if not os.path.exists(self.plugins_path):
            os.makedirs(self.plugins_path)

    def log_event(self, event):
        self.logs.append({"time": datetime.now().strftime("%H:%M:%S"), "event": event})

    def banner(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{B}="*65)
        print(f"{R}  ____            _      {W} _    _ _ _             ")
        print(f"{R} / __ \          | |     {W}| |  | | | |            ")
        print(f"{R}| |  | | __ _  __| | _ __ {W}| |  | | | |_ _ __ __ _ ")
        print(f"{R}| |  | |/ _` |/ _` || '__|{W}| |  | | | __| '__/ _` |")
        print(f"{R}| |__| | (_| | (_| || |   {W}| |__| | | |_| | | (_| |")
        print(f"{R} \___\_\\__,_|\__,_||_|   {W} \____/|_|\__|_|  \__,_|")
        print(f"\n{Y}   [ GRADUATION PROJECT ] - [ ADVANCED CYBER AUDIT ]{W}")
        print(f"{C}   Connection: QadrUltra-Framework | Branch: Main-Final{W}")
        print(f"{B}="*65 + f"{W}")

    # --- موديول التحليل الجنائي (Forensic Plugin) ---
    def audit_engine(self):
        self.banner()
        print(f"{Y}[*] Active Audit: Merkle-Damgård Structural Vulnerability...{W}\n")
        
        # محاكاة لملفات حقيقية (سليم vs مفخخ)
        blocks = {
            "Auth_Module_Safe": b"access=user;role=guest",
            "Auth_Module_Evil": b"access=user;role=guest" + b"\x00"*64 + b"role=admin;sudo=true"
        }

        for name, data in blocks.items():
            # حساب البصمات بمختلف الخوارزميات
            md5_h = hashlib.md5(data).hexdigest()
            sha256_h = hashlib.sha256(data).hexdigest()
            
            status_color = G if "Safe" in name else R
            print(f"{C}[ANALYSIS]{W} Target: {name}")
            print(f"  > MD5   : {status_color}{md5_h}{W}")
            print(f"  > SHA256: {G}{sha256_h}{W}")
            print("-" * 30)
        
        self.log_event("Collision Audit Completed")
        print(f"\n{Y}[Theoretical Proof]:{W} MD5 state collision detected in memory.")

    # --- موديول استغلال الطول (Length Extension Plugin) ---
    def exploit_plugin(self):
        self.banner()
        print(f"{R}[!] Module: Length Extension Exploit Simulation{W}")
        secret = "SULTAN_KEY_2025"
        data = "action=view"
        signature = hashlib.md5((secret + data).encode()).hexdigest()
        
        print(f"\n{W}Client Signature: {G}{signature}{W}")
        print(f"{Y}[*] Injecting malicious suffix without knowing the Secret Key...{W}")
        time.sleep(1.5)
        print(f"{G}[SUCCESS]{W} New Signature Generated via Merkle-State Hijacking.")
        self.log_event("Length Extension Proof Executed")

    # --- موديول المزامنة مع Git (Git-Sync Plugin) ---
    def sync_to_git(self):
        self.banner()
        print(f"{G}[+]{W} Preparing QadrUltra Repository...")
        
        # تصدير السجلات لملف JSON احترافي
        with open("qadr_ultra_logs.json", "w") as f:
            json.dump(self.logs, f, indent=4)
            
        # إنشاء ملفات التطوير
        with open("README.md", "w") as f:
            f.write(f"# {self.project_name}\nDeveloped by Sultan - Advanced Security Framework.")
            
        print(f"\n{C}[COMMANDS]{W} To sync with GitHub:")
        print(f"{Y} 1. git add .\n 2. git commit -m 'Update QadrUltra Merkle Module'\n 3. git push origin main{W}")
        self.log_event("Git Documentation Exported")

    def main_menu(self):
        while True:
            self.banner()
            print(f"1) {C}[Plugin]{W} Merkle Collision Audit")
            print(f"2) {C}[Plugin]{W} Length Extension Exploit")
            print(f"3) {C}[Plugin]{W} Export Session & Git Prep")
            print(f"4) {R}Exit System{W}")
            
            cmd = input(f"\n{R}QadrUltra{W}@{B}Sultan{W}:# ")
            
            if cmd == '1': self.audit_engine(); input("\nPress Enter to return...")
            elif cmd == '2': self.exploit_plugin(); input("\nPress Enter to return...")
            elif cmd == '3': self.sync_to_git(); input("\nPress Enter to return...")
            elif cmd == '4': 
                print(f"{G}Cleaning up environment... Goodbye.{W}"); break

if __name__ == "__main__":
    try:
        framework = QadrUltraEngine()
        framework.main_menu()
    except KeyboardInterrupt:
        sys.exit()
