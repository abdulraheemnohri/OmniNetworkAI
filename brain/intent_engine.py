class IntentEngine:
    def __init__(self):
        self.intents = {
            "COMPUTER_CONTROL": ["open", "close", "process", "system", "pc", "computer", "shutdown"],
            "MOBILE_CONTROL": ["phone", "mobile", "android", "ios", "adb", "screenshot", "tap", "swipe"],
            "ROUTER_CONTROL": ["router", "wifi", "password", "reboot", "restart router", "block mac"],
            "CCTV_CONTROL": ["camera", "cctv", "live", "record", "stream", "onvif"],
            "IOT_CONTROL": ["light", "plug", "sensor", "mqtt", "iot", "smart"],
            "NETWORK_SCAN": ["scan", "network", "discover", "devices", "ip scan"]
        }

    def classify_intent(self, command):
        command = command.lower()
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in command:
                    return intent
        return "UNKNOWN"
