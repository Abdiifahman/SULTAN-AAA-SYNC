"""
Network plugin: collects local network metadata (non-invasive).
Does NOT attempt to crawl or attack other hosts.
"""

import socket
import platform

def run(args):
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = None
    res = {
        "note": "Local network metadata only",
        "hostname": hostname,
        "local_ip": local_ip,
        "platform": platform.platform(),
        "keys": []
    }
    return res