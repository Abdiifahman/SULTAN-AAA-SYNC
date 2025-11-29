import requests
import json
import logging

class AIIntegration:
    def __init__(self, api_url, api_key, model_name='grok-4'):  # افتراضي Grok، لكن يمكن تغيير
        self.api_url = api_url  # مثل 'https://api.x.ai/v1/chat/completions' لـ xAI
        self.api_key = api_key
        self.model_name = model_name

    def analyze_with_ai(self, packet_data, prompt_template="Analyze this network packet for potential AI-related threats: {data}"):
        """إرسال البيانات إلى AI لتحليل إضافي (متكامل مع أي AI مثل Grok)"""
        prompt = prompt_template.format(data=json.dumps(packet_data))
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': self.model_name,
            'messages': [{'role': 'user', 'content': prompt}]
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            ai_response = response.json()['choices'][0]['message']['content']
            logging.info(f"AI analysis: {ai_response}")
            return ai_response
        except Exception as e:
            logging.error(f"Error in AI integration: {e}")
            return None

# مثال استخدام: في response_system.py، استدعِ AIIntegration للرد على الهجمات
# ai = AIIntegration('https://api.x.ai/v1/chat/completions', 'YOUR_API_KEY')
# ai.analyze_with_ai(packet_data)