import os
import argparse
from version1_cloud.operator import CloudAIOperator
from version2_offline.operator import OfflineAIOperator
from version3_hybrid.operator import HybridAIOperator

def main():
    parser = argparse.ArgumentParser(description="OmniOperator AI Suite")
    parser.add_argument("--version", type=int, choices=[1, 2, 3], default=3, help="Version to run: 1 (Cloud), 2 (Offline), 3 (Hybrid)")
    parser.add_argument("--command", type=str, help="Command to execute")
    args = parser.parse_args()

    print(f"🚀 Starting OmniOperator AI (Version {args.version})...")

    if args.version == 1:
        op = CloudAIOperator()
    elif args.version == 2:
        op = OfflineAIOperator()
    else:
        op = HybridAIOperator()

    if args.command:
        result = op.process(args.command)
        print(f"Result: {result}")
    else:
        print("Ready for commands. (Use --command to run a single command or integrate with Telegram)")
        # In a full setup, this would start the TelegramBot or Web Dashboard
        # bot = TelegramBot(os.getenv("TELEGRAM_BOT_TOKEN"))
        # bot.run()

if __name__ == "__main__":
    main()
