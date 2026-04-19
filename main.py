import os
import argparse
import threading
import time
from version1_cloud.operator import CloudAIOperator
from version2_offline.operator import OfflineAIOperator
from version3_hybrid.operator import HybridAIOperator
from shared_core.analytics import AnalyticsSystem
from shared_core.automation import TaskEngine

def background_analytics():
    analytics = AnalyticsSystem()
    task_engine = TaskEngine()
    print("📈 Analytics System: ONLINE")
    while True:
        stats = task_engine.pc.system_monitor()
        analytics.log_metrics(stats['cpu'], stats['memory'])
        time.sleep(60) # Log every minute

def main():
    parser = argparse.ArgumentParser(description="OmniOperator AI Suite")
    parser.add_argument("--version", type=int, choices=[1, 2, 3], default=3)
    parser.add_argument("--command", type=str)
    args = parser.parse_args()

    # Start Analytics Thread
    threading.Thread(target=background_analytics, daemon=True).start()

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
        print("System Kernel Ready. (Integrate via Dashboard or Telegram)")
        # In a real environment, this would keep the process alive
        while True:
            time.sleep(1)

if __name__ == "__main__":
    main()
