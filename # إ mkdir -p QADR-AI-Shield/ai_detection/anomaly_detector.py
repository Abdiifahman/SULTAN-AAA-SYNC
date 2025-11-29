import numpy as np
from sklearn.ensemble import IsolationForest
from tensorflow import keras
import joblib
import logging
import os

logging.basicConfig(level=logging.INFO)  # للوضع المطور: logging مفصل

class AIDetectionEngine:
    def __init__(self, load_models=False):
        self.anomaly_model = IsolationForest(contamination=0.1, random_state=42)
        self.sequence_model = self.build_lstm_model()
        self.is_trained = False
        self.model_dir = 'models/trained_models/'
        os.makedirs(self.model_dir, exist_ok=True)
        if load_models:
            self.load_models()

    def build_lstm_model(self):
        model = keras.Sequential([
            keras.layers.LSTM(64, return_sequences=True, input_shape=(None, 5)),  # 5 features
            keras.layers.Dropout(0.2),
            keras.layers.LSTM(32),
            keras.layers.Dense(16, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def extract_features(self, packet_data):
        """استخراج features من حزم الشبكة"""
        features = [
            packet_data.get('length', len(packet_data)),  # إبداع: استخدم 'length' إن وجد، أو len(dict)
            packet_data.get('timestamp_variance', 0),
            packet_data.get('packet_size_std', 0),
            packet_data.get('protocol_entropy', 0),
            packet_data.get('source_ip_diversity', 0)
        ]
        logging.debug(f"Extracted features: {features}")
        return np.array(features).reshape(1, -1)

    def preprocess_sequence(self, packet_sequence):
        """معالجة التسلسل لـ LSTM (إضافة لتصحيح الخطأ)"""
        features = [self.extract_features(pkt) for pkt in packet_sequence]
        return np.array(features).reshape(1, len(packet_sequence), -1)  # (batch, timesteps, features)

    def detect_anomaly(self, packet_data):
        """كشف anomalies (إضافة جديدة)"""
        if not self.is_trained:
            raise ValueError("النموذج غير مدرب بعد!")
        features = self.extract_features(packet_data)
        prediction = self.anomaly_model.predict(features)
        is_anomaly = prediction == -1
        logging.info(f"Anomaly detection: {is_anomaly}")
        return is_anomaly

    def detect_replay_attack(self, packet_sequence):
        """كشف هجمات replay باستخدام LSTM"""
        if not self.is_trained:
            raise ValueError("النموذج غير مدرب بعد!")
        sequence_features = self.preprocess_sequence(packet_sequence)
        prediction = self.sequence_model.predict(sequence_features)[0][0]
        is_attack = prediction > 0.8  # threshold
        logging.info(f"Replay attack detection: {is_attack} (prob: {prediction})")
        return is_attack

    def train_models(self, normal_traffic, attack_traffic):
        """تدريب النماذج على بيانات طبيعية وهجومية"""
        # تدريب Isolation Forest على الطبيعي فقط (تحسين)
        X_normal = np.vstack([self.extract_features(pkt) for pkt in normal_traffic])
        self.anomaly_model.fit(X_normal)

        # تدريب LSTM على كلاهما (مع تحويل إلى 3D)
        X_attack = np.vstack([self.extract_features(pkt) for pkt in attack_traffic])
        X_train = np.vstack((X_normal, X_attack))
        X_train = np.expand_dims(X_train, axis=1)  # (samples, 1, features) لتسلسلات بسيطة
        y_train = np.array([0] * len(normal_traffic) + [1] * len(attack_traffic))

        self.sequence_model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)
        self.is_trained = True
        self.save_models()
        logging.info("التدريب اكتمل!")

    def save_models(self):
        """حفظ النماذج (إضافة جديدة)"""
        joblib.dump(self.anomaly_model, os.path.join(self.model_dir, 'anomaly_model.pkl'))
        self.sequence_model.save(os.path.join(self.model_dir, 'sequence_model.h5'))

    def load_models(self):
        """تحميل النماذج (إضافة جديدة)"""
        self.anomaly_model = joblib.load(os.path.join(self.model_dir, 'anomaly_model.pkl'))
        self.sequence_model = keras.models.load_model(os.path.join(self.model_dir, 'sequence_model.h5'))
        self.is_trained = True
        logging.info("النماذج محملة!")

# نموذج بيانات تدريب (أضفت 'length' و'source_ip_diversity' للتوافق)
normal_traffic = [
    {'length': 100, 'timestamp_variance': 0.1, 'packet_size_std': 50, 'protocol_entropy': 0.2, 'source_ip_diversity': 0.3},
    {'length': 120, 'timestamp_variance': 0.2, 'packet_size_std': 45, 'protocol_entropy': 0.3, 'source_ip_diversity': 0.4}
]

attack_traffic = [
    {'length': 10, 'timestamp_variance': 0.01, 'packet_size_std': 5, 'protocol_entropy': 0.9, 'source_ip_diversity': 0.05},
    {'length': 15, 'timestamp_variance': 0.02, 'packet_size_std': 8, 'protocol_entropy': 0.85, 'source_ip_diversity': 0.1}
]