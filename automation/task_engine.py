from control.computer.pc_controller import PCController
from control.mobile.adb_controller import ADBController
from control.router.router_controller import RouterController
from network.network_scanner import NetworkScanner
from control.cctv.onvif_client import ONVIFClient
from control.iot.mqtt_client import MQTTClient

class TaskEngine:
    def __init__(self):
        self.pc = PCController()
        self.adb = ADBController()
        self.router = RouterController("192.168.1.1", "admin", "password") # Defaults for now
        self.scanner = NetworkScanner()
        self.cctv = ONVIFClient()
        self.iot = MQTTClient()

    def execute_task(self, intent, command):
        command = command.lower()

        if intent == "COMPUTER_CONTROL":
            if "open" in command:
                app = command.split("open")[-1].strip()
                return self.pc.open_app(app)
            elif "system" in command or "monitor" in command:
                return self.pc.system_monitor()
            else:
                return "Unknown Computer Control command"

        elif intent == "ROUTER_CONTROL":
            if "restart" in command or "reboot" in command:
                return self.router.restart()
            elif "password" in command:
                # Mock password extraction
                return self.router.change_wifi_password("new_secure_password")
            else:
                return "Unknown Router Control command"

        elif intent == "MOBILE_CONTROL":
            if "screenshot" in command:
                return "Executing: adb shell screencap -p /sdcard/screen.png" # Example
            elif "tap" in command:
                return self.adb.tap(100, 200) # Mock coords
            else:
                return "Executing Mobile Control command via ADB"

        elif intent == "NETWORK_SCAN":
            return f"Scan results: {self.scanner.scan_network()}"

        elif intent == "CCTV_CONTROL":
            return f"Cameras: {self.cctv.get_camera_list()}"

        elif intent == "IOT_CONTROL":
            return "Executing IoT command via MQTT"

        else:
            return f"No handler for intent: {intent}"
