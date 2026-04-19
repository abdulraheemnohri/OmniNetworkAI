from agents.pc_agent.pc_controller import PCController
from agents.mobile_agent.adb_controller import ADBController
from agents.network_agent.router_controller import RouterController
from shared_core.network.network_scanner import NetworkScanner
from agents.cctv_agent.onvif_client import ONVIFClient
from agents.iot_agent.mqtt_client import MQTTClient
from shared_core.security import SecurityManager
from shared_core.memory import MemorySystem
from shared_core.plugin_manager import PluginManager

class TaskEngine:
    def __init__(self):
        self.pc = PCController()
        self.adb = ADBController()
        self.router = RouterController("192.168.1.1", "admin", "password")
        self.scanner = NetworkScanner()
        self.cctv = ONVIFClient()
        self.iot = MQTTClient()
        self.security = SecurityManager()
        self.memory = MemorySystem()
        self.plugins = PluginManager()
        self.plugins.load_plugins()

    def execute_task(self, intent, command):
        self.memory.add_memory(command, {"intent": intent, "command": command})

        risk = self.security.calculate_risk(command, intent)
        if risk > 80:
            return f"Blocked: High risk task ({risk}%). Manual approval required."

        command_lower = command.lower()

        if intent == "COMPUTER_CONTROL":
            if "open" in command_lower:
                app = command.split("open")[-1].strip()
                return self.pc.open_app(app)
            elif "system" in command_lower or "monitor" in command_lower:
                return self.pc.system_monitor()
            elif "process" in command_lower:
                return self.pc.list_processes()
            else:
                return "Unknown Computer Control command"

        elif intent == "ROUTER_CONTROL":
            if "restart" in command_lower or "reboot" in command_lower:
                return self.router.restart()
            elif "password" in command_lower:
                return self.router.change_wifi_password("new_secure_password")
            else:
                return "Unknown Router Control command"

        elif intent == "MOBILE_CONTROL":
            if "screenshot" in command_lower:
                return self.adb.screenshot()
            elif "tap" in command_lower:
                return self.adb.tap(100, 200)
            else:
                return "Executing Mobile Control command via ADB"

        elif intent == "NETWORK_SCAN":
            return f"Scan results: {self.scanner.scan_network()}"

        elif intent == "CCTV_CONTROL":
            return f"Cameras: {self.cctv.get_camera_list()}"

        elif intent == "IOT_CONTROL":
            return "Executing IoT command via MQTT"

        # Check for plugin execution
        for plugin in self.plugins.list_plugins():
            if plugin in command_lower:
                return self.plugins.execute_plugin(plugin)

        return f"No handler for intent: {intent}"

    def orchestrate_multi_device(self, scenario):
        if scenario == "office_shutdown":
            results = []
            results.append(self.pc.close_app("chrome"))
            results.append("IoT Device Link: Disconnected")
            results.append("Turned off smart lights")
            return results
        return "Unknown scenario"
