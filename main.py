import os
from comms.telegram_bot import TelegramBot
from brain.offline_model import OfflineAIBrain
import threading

def run_bot(token):
    bot = TelegramBot(token)
    bot.run()

def main():
    print("🚀 Starting OmniNetwork AI Operator (ONAIO)...")

    # Load environment variables or use defaults
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

    if telegram_token == "YOUR_TELEGRAM_BOT_TOKEN":
        print("⚠️ Warning: TELEGRAM_BOT_TOKEN not set. Telegram features will not work.")
    else:
        # Start Telegram Bot in a separate thread if needed,
        # but Application.run_polling() is blocking, so we'll just run it if it's the main interface.
        run_bot(telegram_token)

if __name__ == "__main__":
    main()
