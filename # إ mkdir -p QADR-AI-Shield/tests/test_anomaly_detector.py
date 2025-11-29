import unittest
from ai_detection.anomaly_detector import AIDetectionEngine, normal_traffic, attack_traffic
import numpy as np

class TestAIDetectionEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AIDetectionEngine()

    def test_extract_features(self):
        packet = {'length': 100, 'timestamp_variance': 0.1, 'packet_size_std': 50, 'protocol_entropy': 0.2, 'source_ip_diversity': 0.3}
        features = self.engine.extract_features(packet)
        self.assertEqual(features.shape, (1, 5))

    def test_train_models(self):
        self.engine.train_models(normal_traffic, attack_traffic)
        self.assertTrue(self.engine.is_trained)

    def test_detect_anomaly(self):
        self.engine.train_models(normal_traffic, attack_traffic)
        normal_packet = normal_traffic[0]
        attack_packet = attack_traffic[0]
        self.assertFalse(self.engine.detect_anomaly(normal_packet))  # يجب أن يكون طبيعي
        self.assertTrue(self.engine.detect_anomaly(attack_packet))   # يجب أن يكون anomaly (قد يختلف بناءً على التدريب)

    def test_detect_replay_attack(self):
        self.engine.train_models(normal_traffic, attack_traffic)
        normal_seq = normal_traffic
        attack_seq = attack_traffic
        self.assertFalse(self.engine.detect_replay_attack(normal_seq))
        self.assertTrue(self.engine.detect_replay_attack(attack_seq))

if __name__ == '__main__':
    unittest.main()