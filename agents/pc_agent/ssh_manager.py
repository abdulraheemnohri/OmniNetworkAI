import paramiko

class SSHManager:
    def __init__(self, host, username, password=None, key_filename=None):
        self.host = host
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def execute_command(self, command):
        try:
            self.client.connect(self.host, username=self.username, password=self.password, key_filename=self.key_filename)
            stdin, stdout, stderr = self.client.exec_command(command)
            return stdout.read().decode()
        except Exception as e:
            return f"SSH Error: {e}"
        finally:
            self.client.close()
