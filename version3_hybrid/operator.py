from ai_brain.offline_model.model import OfflineAIBrain
from ai_brain.online_router.router import OnlineRouter
from shared_core.automation import TaskEngine
from shared_core.command_parser import CommandParser

class HybridAIOperator:
    def __init__(self):
        self.online_brain = OnlineRouter()
        self.task_engine = TaskEngine()
        self.parser = CommandParser()

    def process(self, command, complexity="simple"):
        if complexity == "complex":
            return self.online_brain.route_task(command, complexity="complex")

        intent = self.parser.classify_intent(command)
        if intent != "UNKNOWN":
            return self.task_engine.execute_task(intent, command)

        # Fallback to online if offline fails or is simple but unknown
        return self.online_brain.route_task(command, complexity="complex")
