from twilio.rest import Client
from shared_core.automation import TaskEngine
from shared_core.command_parser import CommandParser

class WhatsAppBridge:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = f"whatsapp:{from_number}"
        self.task_engine = TaskEngine()
        self.parser = CommandParser()

    def send_message(self, to_number, body):
        message = self.client.messages.create(
            body=body,
            from_=self.from_number,
            to=f"whatsapp:{to_number}"
        )
        return message.sid

    def handle_incoming(self, from_number, body):
        intent = self.parser.classify_intent(body)
        result = self.task_engine.execute_task(intent, body)
        self.send_message(from_number, f"Operator Response: {result}")
