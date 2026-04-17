from shared_core.network.network_scanner import NetworkScanner
import sqlite3

class DeviceRegistry:
    def __init__(self, db_path="devices.db"):
        self.scanner = NetworkScanner()
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("CREATE TABLE IF NOT EXISTS devices (ip TEXT PRIMARY KEY, mac TEXT, vendor TEXT, status TEXT, last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        conn.commit()
        conn.close()

    def discover_devices(self, subnet="192.168.1.0/24"):
        devices = self.scanner.scan_network(subnet)
        conn = sqlite3.connect(self.db_path)
        for ip, info in devices.items():
            conn.execute("INSERT OR REPLACE INTO devices (ip, mac, vendor, status) VALUES (?, ?, ?, ?)",
                         (ip, info['mac'], info['vendor'], info['status']))
        conn.commit()
        conn.close()
        return devices

    def list_all_devices(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT * FROM devices")
        devices = cursor.fetchall()
        conn.close()
        return devices
