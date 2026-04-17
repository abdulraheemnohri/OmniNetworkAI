import psutil
import subprocess
import os

class PCController:
    def __init__(self):
        pass

    def open_app(self, app_name):
        try:
            # Platform dependent
            if os.name == 'nt': # Windows
                subprocess.Popen(['start', app_name], shell=True)
            elif os.name == 'posix': # Linux/Mac
                subprocess.Popen(['xdg-open', app_name] if os.uname().sysname == 'Linux' else ['open', app_name])
            return f"Opened {app_name}"
        except Exception as e:
            return f"Failed to open {app_name}: {e}"

    def close_app(self, app_name):
        for proc in psutil.process_iter(['name']):
            if app_name.lower() in proc.info['name'].lower():
                proc.kill()
                return f"Closed {app_name}"
        return f"App {app_name} not found"

    def system_monitor(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        return f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%"

    def list_processes(self):
        processes = [proc.info['name'] for proc in psutil.process_iter(['name'])]
        return f"Processes: {', '.join(processes[:10])}..."
