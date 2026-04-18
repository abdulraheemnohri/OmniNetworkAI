from twilio.rest import Client
import os

class WhatsAppBridge:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = f"whatsapp:{from_number}"

    def send_message(self, to_number, body):
        try:
            message = self.client.messages.create(
                body=body,
                from_=self.from_number,
                to=f"whatsapp:{to_number}"
            )
            return message.sid
        except Exception as e:
            return f"WhatsApp Error: {e}"

    def format_status_report(self, stats):
        return (
            f"📱 *OmniOperator System Report*\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🖥️ CPU: {stats['cpu']}%\n"
            f"🧠 MEM: {stats['memory']}%\n"
            f"🌐 Net: PROTECTED\n"
            f"━━━━━━━━━━━━━━━━━━━"
        )
