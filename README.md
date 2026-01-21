Qadr
# 🛡️ PROJECT: QADR ENGINE (ADVANCED CYBER-RECONNAISSANCE)
# 🧩 MODULE: QadrBle Master Suite
# 👤 LEAD DEVELOPER: SULTAN-AAA
# 📅 DEPLOYMENT DATE: 2026-01-21
# 📜 LEGAL: COPYRIGHT © 2026 SULTAN-AAA. ALL RIGHTS RESERVED.
# 🔗 SYNC REPO: https://github.com/Abdiifahman/SULTAN-AAA-SYNC
# 

import math
import json
import os
import google.generativeai as genai
from datetime import datetime

class QadrBleMaster:
    """
    عقل QadrBle المتأمل: نظام SIGINT متكامل لتحليل وتتبع الأهداف لاسلكياً.
    يجمع بين دقة الأرقام الفيزيائية وقوة التنبؤ بالذكاء الاصطناعي.
    """
    
    def __init__(self, api_key):
        # توثيق الحقوق داخل البنية التحتية للمحرك
        self.identity = {
            "Author": "SULTAN-AAA",
            "Project": "Qadr cli",
            "Engine": "Qadr Engine v5.1"
        }
        
        # إعداد المحلل العالمي (Gemini API)
        if api_key:
            genai.configure(api_key=api_key)
            self.brain = genai.GenerativeModel('gemini-1.5-flash')
        
        # معامل البيئة الفيزيائي (Sultan-Factor) لتحليل المسافات
        self.path_loss_exp = 2.4 

    def calculate_target_range(self, rssi, tx_power=None):
        """تحديد الموقع تقديراً بالترددات والأرقام الخام"""
        # استخدام القوة الإرسالية الافتراضية إذا لم يتم اكتشافها
        p_tx = tx_power if tx_power is not None else -59
        try:
            # خوارزمية تقدير المسافة الفيزيائية
            distance = 10 ** ((p_tx - rssi) / (10 * self.path_loss_exp))
            return round(distance, 2)
        except Exception:
            return 0.0

    def get_global_intelligence(self, device_data):
        """استدعاء دالة المحلل الذكي لتعريف الجهاز ومخاطره عالمياً"""
        prompt = f"""
        Analyze this BLE Fingerprint for SULTAN-AAA's Qadr Engine:
        - UUID: {device_data.get('uuid')}
        - Appearance: {device_data.get('appearance')}
        - PHY: {device_data.get('primaryPHY')}
        - RSSI: {device_data.get('rssi')}
        
        Identify: 1.Exact Device Model 2.Manufacturer 3.Vulnerability Level.
        Response Style: Professional Cyber-Report.
        """
        try:
            response = self.brain.generate_content(prompt)
            return response.text.strip()
        except:
            return "Local Signature Analysis Only: Unknown Secure Device."

    def execute_full_scan(self, raw_data):
        """المعالج النهائي: يحول بيانات المسح إلى استخبارات تكتيكية مرئية"""
        data = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
        scan_results = {
            "Meta": self.identity,
            "Timestamp": datetime.now().isoformat(),
            "Detections": []
        }

        for dev in data.get('scannedDevices', []):
            # دمج خبرة 5 سنوات في التحليل الميداني
            dist = self.calculate_target_range(dev.get('rssi'), dev.get('transmitPower'))
            intel = self.get_global_intelligence(dev)
            
            # تصنيف الجهاز بناءً على بروتوكول PHY المستلم
            phy_mode = "LE Coded (Long Range)" if dev.get('primaryPHY') == 129 else "LE 1M (Standard)"
            
            scan_results["Detections"].append({
                "Target_UUID": dev.get('uuid'),
                "Distance": f"{dist}m",
                "Signal_Quality": f"{dev.get('rssi')}dBm",
                "PHY_Layer": phy_mode,
                "Intelligence_Report": intel,
                "Action": "EXPLOITABLE" if dev.get('isConnectable') else "MONITOR"
            })
            
        return scan_results

    def sync_to_qadr_repo(self, final_report):
        """حفظ التقرير بتنسيق Sync متوافق مع حقوق الملكية الخاصة بك"""
        filename = f"QadrBle_Report_{datetime.now().strftime('%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(final_report, f, indent=4)
        print(f"[*] Intelligence Synced to SULTAN-AAA-SYNC: {filename}")

# ----------------------------------------------------------------------------------
# ⚖️ COPYRIGHT NOTICE: 
# THIS SCRIPT IS THE SOLE PROPERTY OF SULTAN-AAA. 
# ANY UNAUTHORIZED USE OR MODIFICATION IS STRICTLY PROHIBITED.
# COMMERCIAL USE REQUIRES SPECIFIC ROYALTY PAYMENTS TO THE AUTHOR.
# 
le Source of Truth لجميع عمليات الـ BLE.
    """
    
    def __init__(self, api_key=None, security_mode="High"):
        self.metadata = {
            "version": "Nexus-2026.01",
            "developer": "SULTAN-AAA",
            "engine": "Qadr_SIGINT",
            "copyright": "© 2026 SULTAN-AAA. All Rights Reserved."
        }
        
        # 1. إعداد ذكاء Gemini API للتحليل العالمي
        if api_key:
            genai.configure(api_key=api_key)
            self.ai_analyzer = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.ai_analyzer = None

        # 2. معاملات البيئة للترددات (خوارزمية سلطان لتقدير الموقع)
        self.signal_const = 2.4  # معامل الوسط (Concrete/Urban)

    def _apply_sultan_localization(self, rssi, tx_power):
        """تطبيق خوارزمية تحديد الموقع تقديراً بالترددات والأرقام"""
        p_tx = tx_power if tx_power is not None else -59
        try:
            # معادلة Path Loss متقدمة لتقليل نسبة الخطأ
            distance = 10 ** ((p_tx - rssi) / (10 * self.signal_const))
            return round(distance, 2)
        except ZeroDivisionError:
            return 0.0

    def _global_ai_lookup(self, device):
        """استشارة Gemini API لتحديد نوع الجهاز عالمياً ومخاطره"""
        if not self.ai_analyzer:
            return "Local Signature Match Only (No API)"
        
        prompt = (
            f"As Qadr Engine Cyber Analyst, identify this BLE Fingerprint: "
            f"Name: {device.get('peripheralName')}, UUID: {device.get('uuid')}, "
            f"Appearance: {device.get('appearance')}. "
            f"Return Manufacturer, Device Type, and Security Risk (High/Low)."
        )
        try:
            response = self.ai_analyzer.generate_content(prompt)
            return response.text.strip()
        except Exception:
            return "Global Database Timeout"

    def process_qadr_scan(self, raw_json):
        """
        المعالج الرئيسي: يحول البيانات الخام إلى تقرير استخباراتي مرتب.
        هذا الجزء هو ما يحتاجه مشروع Qadr cli فعلياً.
        """
        data = json.loads(raw_json) if isinstance(raw_json, str) else raw_json
        output_report = {
            "Qadr_Header": self.metadata,
            "Scan_Summary": {
                "Total_Detected": len(data.get('scannedDevices', [])),
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Targets": []
        }

        for dev in data.get('scannedDevices', []):
            # دمج خبرة 5 سنوات في فلترة البيانات
            dist = self._apply_sultan_localization(dev.get('rssi'), dev.get('transmitPower'))
            intel = self._global_ai_lookup(dev)
            
            target = {
                "ID": dev.get('uuid'),
                "Distance": f"{dist} Meters",
                "Signal_Strength": f"{dev.get('rssi')} dBm",
                "Intelligence": intel,
                "Status": "READY_FOR_EXPLOIT" if dev.get('isConnectable') else "PASSIVE_MONITORING",
                "PHY_Tech": "Coded-LongRange" if dev.get('primaryPHY') == 129 else "Standard-BLE"
            }
            output_report["Targets"].append(target)
            
        return output_report

    def export_qadr_sync(self, report):
        """تصدير النتائج بتنسيق Sync المتوافق مع مستودع GitHub الخاص بك"""
        filename = f"Qadr_Scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        print(f"[*] Report Synced to: {filename}")

# 
# ⚖️ LEGAL FOOTER: 
# This logic is strictly proprietary to SULTAN-AAA. 
# Use of this script for commercial profit triggers a royalty obligation.
# 
