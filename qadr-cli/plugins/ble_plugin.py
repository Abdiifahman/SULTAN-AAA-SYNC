"""
Example BLE plugin (simulated) — returns local BLE scan summary.
Note: On iOS this is a placeholder; real BLE scanning on iOS requires a native app.
Keep this plugin safe (no exploitation).
"""

def run(args):
    # Simulated result — replace with a harmless, authorized scan from a proper environment
    result = {
        "note": "Simulated BLE scan (no raw exploit). Real scanning requires native app permissions.",
        "devices": [
            {"name": "sim-beacon-1", "rssi": -60, "id": "BEACON-001"},
            {"name": "sim-beacon-2", "rssi": -78, "id": "BEACON-002"},
        ],
        "keys": []  # intentionally empty in example
    }
    return result