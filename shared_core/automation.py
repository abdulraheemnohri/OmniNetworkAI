from agents.pc_agent.pc_controller import PCController
from agents.mobile_agent.adb_controller import ADBController
from agents.network_agent.router_controller import RouterController
from shared_core.network.network_scanner import NetworkScanner
from agents.cctv_agent.onvif_client import ONVIFClient
from agents.iot_agent.mqtt_client import MQTTClient
from shared_core.security import SecurityManager

class TaskEngine:
    def __init__(self):
        self.pc = PCController()
        self.adb = ADBController()
        self.router = RouterController("192.168.1.1", "admin", "password")
        self.scanner = NetworkScanner()
        self.cctv = ONVIFClient()
        self.iot = MQTTClient()
        self.security = SecurityManager()

    def execute_task(self, intent, command):
        risk = self.security.calculate_risk(command, intent)
        if risk > 80:
            return f"Blocked: High risk task ({risk}%). Manual approval required."

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
                return self.router.change_wifi_password("new_secure_password")
            else:
                return "Unknown Router Control command"

        elif intent == "MOBILE_CONTROL":
            if "screenshot" in command:
                return self.adb.screenshot()
            elif "tap" in command:
                return self.adb.tap(100, 200)
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
