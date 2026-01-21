# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------
# 🛡️ SYSTEM: QADR ENGINE (CYBER-INTELLIGENCE CLI)
# 🧩 MODULE: QadrBle NEXUS - FINAL MASTER CORE
# 👤 AUTHOR: SULTAN-AAA (Lead Developer)
# 📅 UPDATED: 2026-01-21
# 📜 LICENSE: PROPRIETARY - SULTAN-AAA-SYNC (Royalties Required for Commercial Use)
# 🌐 REPO: https://github.com/Abdiifahman/SULTAN-AAA-SYNC
# ----------------------------------------------------------------------------------

import math
import json
import os
import sys
import google.generativeai as genai
from datetime import datetime

class QadrBleNexus:
    """
    العقل المدبر لـ Qadr Engine: يدمج تتبع الترددات بالذكاء الاصطناعي العالمي.
    تم تصميمه ليعمل كـ Single Source of Truth لجميع عمليات الـ BLE.
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

# ----------------------------------------------------------------------------------
# ⚖️ LEGAL FOOTER: 
# This logic is strictly proprietary to SULTAN-AAA. 
# Use of this script for commercial profit triggers a royalty obligation.
# ----------------------------------------------------------------------------------
