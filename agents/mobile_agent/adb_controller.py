import subprocess

class ADBController:
    def __init__(self):
        pass

    def run_command(self, cmd):
        try:
            result = subprocess.run(['adb'] + cmd.split(), capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"ADB Error: {e}"

    def launch_app(self, package_name):
        return self.run_command(f"shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1")

    def tap(self, x, y):
        return self.run_command(f"shell input tap {x} {y}")

    def swipe(self, x1, y1, x2, y2, duration=500):
        return self.run_command(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")

    def screenshot(self, path="/sdcard/screen.png"):
        self.run_command(f"shell screencap -p {path}")
        return f"Screenshot saved to {path}"

    def pull_file(self, remote_path, local_path):
        return self.run_command(f"pull {remote_path} {local_path}")
