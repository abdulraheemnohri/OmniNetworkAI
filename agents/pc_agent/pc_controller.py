import psutil
import subprocess
import os
import shutil

class PCController:
    def __init__(self):
        pass

    def open_app(self, app_name):
        try:
            if os.name == 'nt':
                subprocess.Popen(['start', app_name], shell=True)
            elif os.name == 'posix':
                subprocess.Popen(['xdg-open', app_name] if os.uname().sysname == 'Linux' else ['open', app_name])
            return f"Opened {app_name}"
        except Exception as e:
            return f"Failed to open {app_name}: {e}"

    def close_app(self, app_name):
        killed = False
        for proc in psutil.process_iter(['name']):
            if app_name.lower() in proc.info['name'].lower():
                proc.kill()
                killed = True
        return f"Closed {app_name}" if killed else f"App {app_name} not found"

    def system_monitor(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        return {"cpu": cpu, "memory": memory, "disk": disk}

    def file_operations(self, action, path, destination=None):
        try:
            if action == "list":
                return os.listdir(path)
            elif action == "delete":
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                return f"Deleted {path}"
            elif action == "move":
                shutil.move(path, destination)
                return f"Moved {path} to {destination}"
            return "Unknown file action"
        except Exception as e:
            return f"File Error: {e}"

    def execute_script(self, script_path):
        try:
            result = subprocess.run(['python3', script_path], capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"Script Error: {e}"
