from comms.telegram_bot import TelegramBot
from comms.whatsapp_bridge import WhatsAppBridge
from shared_core.config import ConfigManager

class BridgeManager:
    def __init__(self):
        self.config = ConfigManager()
        self.telegram = TelegramBot(self.config.get("telegram_token"))
        self.whatsapp = WhatsAppBridge(
            self.config.get("twilio_sid"),
            self.config.get("twilio_token"),
            self.config.get("twilio_number")
        )

    def notify_all(self, message):
        # Example: send critical alert to both
        self.telegram.app.bot.send_message(chat_id="ADMIN_ID", text=message)
        self.whatsapp.send_message("ADMIN_PHONE", message)
