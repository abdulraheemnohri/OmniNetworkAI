from ai_brain.offline_model.ollama_client import OllamaClient
from shared_core.automation import TaskEngine
from shared_core.command_parser import CommandParser

class OfflineAIOperator:
    def __init__(self):
        self.ollama = OllamaClient()
        self.task_engine = TaskEngine()
        self.parser = CommandParser()

    def process(self, command):
        # 1. Try to understand with intent engine first
        intent = self.parser.classify_intent(command)

        if intent != "UNKNOWN":
            # 2. Execute directly if intent is clear
            return self.task_engine.execute_task(intent, command)
        else:
            # 3. Use local Ollama for reasoning if intent is unknown
            print("Reasoning with local Ollama...")
            return self.ollama.generate(command)
