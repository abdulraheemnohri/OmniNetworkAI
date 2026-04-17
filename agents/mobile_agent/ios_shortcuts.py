import subprocess

class IOSShortcuts:
    def __init__(self):
        pass

    def run_shortcut(self, shortcut_name, input_data=None):
        try:
            # Using 'shortcuts' command available on macOS if the mobile is connected/simulated
            # Or triggering via an API/bridge for real iOS devices (limited)
            cmd = ['shortcuts', 'run', shortcut_name]
            if input_data:
                cmd.extend(['-i', input_data])
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"iOS Shortcut Error: {e}"

    def list_shortcuts(self):
        try:
            result = subprocess.run(['shortcuts', 'list'], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"Error listing shortcuts: {e}"
