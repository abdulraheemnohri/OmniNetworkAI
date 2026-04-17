from brain.offline_model import OfflineAIBrain
from control.router.router_controller import RouterController
from comms.telegram_bot import TelegramBot

def main():
    # Initialize AI Brain
    brain = OfflineAIBrain()

    # Initialize Device Controllers
    router = RouterController("192.168.1.1", "admin", "password")

    # Initialize Telegram Bot
    bot = TelegramBot("YOUR_TELEGRAM_BOT_TOKEN")

    # Example: Process a command
    command = "Restart the router"
    response = brain.process_command(command)
    print(f"AI Response: {response}")

    # Execute command
    if "restart" in command.lower() and "router" in command.lower():
        result = router.restart()
        print(f"Router Result: {result}")

    # Start Telegram Bot
    bot.run()

if __name__ == "__main__":
    main()