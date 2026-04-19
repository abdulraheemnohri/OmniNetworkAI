import sqlite3
from datetime import datetime

class AnalyticsSystem:
    def __init__(self, db_path="analytics.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_load REAL,
                mem_usage REAL,
                net_traffic REAL
            )
        """)
        conn.commit()
        conn.close()

    def log_metrics(self, cpu, mem, net=0.0):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO metrics (cpu_load, mem_usage, net_traffic) VALUES (?, ?, ?)", (cpu, mem, net))
        conn.commit()
        conn.close()

    def get_history(self, limit=50):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
        data = cursor.fetchall()
        conn.close()
        return data
