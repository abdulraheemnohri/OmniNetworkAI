from ai_brain.offline_model.model import OfflineAIBrain
from shared_core.automation import TaskEngine
from shared_core.command_parser import CommandParser

class OfflineAIOperator:
    def __init__(self):
        # self.offline_brain = OfflineAIBrain() # Might be heavy to load every time in mock
        self.task_engine = TaskEngine()
        self.parser = CommandParser()

    def process(self, command):
        intent = self.parser.classify_intent(command)
        if intent != "UNKNOWN":
            return self.task_engine.execute_task(intent, command)
        return "Offline model could not understand the command."
