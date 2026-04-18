class OnlineRouter:
    def __init__(self, config=None):
        self.config = config or {}
        self.providers = [
            "OpenAI", "Gemini", "Claude", "Groq",
            "OpenRouter", "Perplexity", "Mistral", "Cohere"
        ]

    def route_task(self, task, complexity="simple"):
        if complexity == "simple":
            return "OFFLINE"

        # Priority mapping
        if "security" in task.lower() or "diagnostic" in task.lower():
            return self.call_provider("Claude", task)
        elif "code" in task.lower() or "script" in task.lower():
            return self.call_provider("OpenAI", task)
        elif "creative" in task.lower():
            return self.call_provider("Gemini", task)
        elif "speed" in task.lower():
            return self.call_provider("Groq", task)
        else:
            return self.call_provider("OpenRouter", task)

    def call_provider(self, provider_name, task):
        key = self.config.get(f"{provider_name.lower()}_api_key", "MOCK_KEY")
        # Ensure at least 5 chars for the key display or use mock
        display_key = key[:5] if len(key) >= 5 else key
        return f"RESPONSE from {provider_name} (Using Key: {display_key}...): Processed task: {task}"
