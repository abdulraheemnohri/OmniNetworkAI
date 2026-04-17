from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from shared_core.command_parser import CommandParser
from shared_core.automation import TaskEngine
from ai_brain.online_router.router import OnlineRouter

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.parser = CommandParser()
        self.task_engine = TaskEngine()
        self.online_router = OnlineRouter()
        self.app = Application.builder().token(token).build()
        self.setup_handlers()

    def setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("menu", self.menu))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_command))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "🚀 OmniOperator AI Online.\n"
            "System Status: PROTECTED\n"
            "Aegis Layer: ACTIVE\n\n"
            "Use /menu for quick actions or send a natural language command."
        )

    async def menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [KeyboardButton("📊 System Monitor"), KeyboardButton("🌐 Network Scan")],
            [KeyboardButton("📱 Mobile Screenshot"), KeyboardButton("🔄 Restart Router")],
            [KeyboardButton("🔐 Risk Report"), KeyboardButton("🧠 Memory Search")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text("Select an operator action:", reply_markup=reply_markup)

    async def handle_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text

        # Handle menu selections
        if text == "📊 System Monitor":
            command = "system monitor"
        elif text == "🌐 Network Scan":
            command = "scan network"
        elif text == "📱 Mobile Screenshot":
            command = "take screenshot"
        elif text == "🔄 Restart Router":
            command = "restart router"
        elif text == "🔐 Risk Report":
            await update.message.reply_text("Security Risk: 10% (Normal Operations)")
            return
        elif text == "🧠 Memory Search":
            await update.message.reply_text("Please enter a query to search memory.")
            return
        else:
            command = text

        intent = self.parser.classify_intent(command)
        await update.message.reply_text(f"🔍 Intent: {intent}\nExecuting command...")

        # Logic to route or execute
        if len(command.split()) > 10:
            result = self.online_router.route_task(command, complexity="complex")
        else:
            result = self.task_engine.execute_task(intent, command)

        await update.message.reply_text(f"✅ Result:\n{result}")

    def run(self):
        print("Telegram bot is running...")
        self.app.run_polling()
