import paramiko

class RouterController:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.ssh.connect(self.ip, username=self.username, password=self.password)
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def restart(self):
        if not self.connect():
            return "Failed to connect to router."
        stdin, stdout, stderr = self.ssh.exec_command("reboot")
        return stdout.read().decode()

    def change_wifi_password(self, new_password):
        if not self.connect():
            return "Failed to connect to router."
        commands = [
            f"uci set wireless.@wifi-iface[0].key='{new_password}'",
            "uci commit",
            "wifi"
        ]
        for cmd in commands:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode()