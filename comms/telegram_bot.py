from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from brain.intent_engine import IntentEngine
from automation.task_engine import TaskEngine
from brain.online_router import OnlineRouter

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.intent_engine = IntentEngine()
        self.task_engine = TaskEngine()
        self.online_router = OnlineRouter()
        self.app = Application.builder().token(token).build()
        self.setup_handlers()

    def setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_command))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Welcome to OmniNetwork AI! Send a command (e.g., 'Restart router', 'Open Chrome', 'Scan network').")

    async def handle_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text
        intent = self.intent_engine.classify_intent(command)

        # Risk Scoring Mock
        risk_score = 0
        if intent in ["ROUTER_CONTROL", "COMPUTER_CONTROL"] and "shutdown" in command.lower():
            risk_score = 80 # High risk

        if risk_score > 50:
            await update.message.reply_text(f"⚠️ HIGH RISK COMMAND DETECTED: '{command}'. Please confirm manually.")
            return

        await update.message.reply_text(f"Intent detected: {intent}. Executing...")

        # Check for complexity
        if len(command.split()) > 10: # Simple heuristic for complex tasks
            response = self.online_router.route_task(command, complexity="complex")
        else:
            response = self.task_engine.execute_task(intent, command)

        await update.message.reply_text(f"Result: {response}")

    def run(self):
        print("Telegram bot is starting...")
        self.app.run_polling()
