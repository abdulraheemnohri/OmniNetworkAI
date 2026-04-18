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

        task_lower = task.lower()
        if "security" in task_lower or "diagnostic" in task_lower:
            return self.call_provider("Claude", task)
        elif "code" in task_lower or "script" in task_lower:
            return self.call_provider("OpenAI", task)
        elif "creative" in task_lower or "explain" in task_lower:
            return self.call_provider("Gemini", task)
        elif "speed" in task_lower or "fast" in task_lower:
            return self.call_provider("Groq", task)
        elif "web" in task_lower or "search" in task_lower:
            return self.call_provider("Perplexity", task)
        elif "mistral" in task_lower or "french" in task_lower:
            return self.call_provider("Mistral", task)
        else:
            return self.call_provider("OpenRouter", task)

    def call_provider(self, provider_name, task):
        key_name = f"{provider_name.lower()}_api_key"
        key = self.config.get(key_name, "MOCK_KEY")

        # Integration logic (placeholder for SDK calls)
        if provider_name == "OpenRouter":
            return f"[OpenRouter] Delegating task to best available model: {task}"

        return f"[{provider_name}] API Call Success with Key {key[:5]}... Task: {task}"
