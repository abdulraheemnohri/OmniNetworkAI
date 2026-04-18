import os
import json

class ConfigManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return self._default_config()

    def _default_config(self):
        return {
            "version": 3,
            "telegram_token": "YOUR_TOKEN",
            "router_ip": "192.168.1.1",
            "router_user": "admin",
            "router_pass": "password",
            "api_port": 8000,
            "security_secret": "ONAIO_SECRET"
        }

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()
