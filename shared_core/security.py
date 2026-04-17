class SecurityManager:
    def __init__(self):
        self.whitelist = ["127.0.0.1", "192.168.1.5"] # Example

    def authenticate_user(self, user_id):
        # In a real app, check against a DB
        return True

    def calculate_risk(self, command, intent):
        command = command.lower()
        if "shutdown" in command or "format" in command or "delete" in command:
            return 90
        if "reboot" in command or "restart" in command:
            return 40
        return 10

    def is_device_whitelisted(self, ip):
        return ip in self.whitelist
