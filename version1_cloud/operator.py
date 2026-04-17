from ai_brain.online_router.router import OnlineRouter
from shared_core.automation import TaskEngine
from shared_core.command_parser import CommandParser

class CloudAIOperator:
    def __init__(self):
        self.online_brain = OnlineRouter()
        self.task_engine = TaskEngine()
        self.parser = CommandParser()

    def process(self, command):
        # Everything is complex for cloud-only version or delegated to API
        response = self.online_brain.route_task(command, complexity="complex")
        # In a real cloud version, we'd extract the intent from the cloud response
        # For now, we still use the parser to map to local agents
        intent = self.parser.classify_intent(command)
        if intent != "UNKNOWN":
            execution_result = self.task_engine.execute_task(intent, command)
            return f"{response}\nLocal Execution: {execution_result}"
        return response
