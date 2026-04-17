from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.updater = Updater(token=token, use_context=True)
        self.setup_handlers()

    def setup_handlers(self):
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.handle_command))

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("Welcome to OmniNetwork AI! Send a command (e.g., 'Restart router').")

    def handle_command(self, update: Update, context: CallbackContext):
        command = update.message.text
        response = f"Executing: {command}"
        update.message.reply_text(response)

    def run(self):
        self.updater.start_polling()
        print("Telegram bot is running...")