import jwt
import datetime

class SecurityManager:
    def __init__(self, secret_key="ONAIO_SECRET"):
        self.secret_key = secret_key
        self.whitelist = ["127.0.0.1", "192.168.1.5"]

    def generate_token(self, user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def calculate_risk(self, command, intent):
        command = command.lower()
        if any(word in command for word in ["shutdown", "format", "delete", "wipe"]):
            return 90
        if any(word in command for word in ["reboot", "restart", "block"]):
            return 40
        return 10

    def is_device_whitelisted(self, ip):
        return ip in self.whitelist
