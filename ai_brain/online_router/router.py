class OnlineRouter:
    def __init__(self, config=None):
        self.config = config or {}
        self.providers = [
            "OpenAI", "Gemini", "Claude", "Groq",
            "OpenRouter", "Perplexity", "Mistral", "Cohere",
            "JulesAPI", "Puter", "ApiFreeLLM", "Routeway", "Zai"
        ]

    def route_task(self, task, complexity="simple"):
        if complexity == "simple":
            return "OFFLINE"

        task_lower = task.lower()

        # New Providers Routing
        if "free" in task_lower or "no-cost" in task_lower:
            return self.call_provider("ApiFreeLLM", task)
        elif "puter" in task_lower:
            return self.call_provider("Puter", task)
        elif "jules" in task_lower:
            return self.call_provider("JulesAPI", task)
        elif "glm" in task_lower or "routeway" in task_lower:
            return self.call_provider("Routeway", task)
        elif "zai" in task_lower:
            return self.call_provider("Zai", task)

        # Legacy Providers Routing
        if "security" in task_lower or "diagnostic" in task_lower:
            return self.call_provider("Claude", task)
        elif "code" in task_lower or "script" in task_lower:
            return self.call_provider("OpenAI", task)
        elif "creative" in task_lower:
            return self.call_provider("Gemini", task)
        else:
            return self.call_provider("OpenRouter", task)

    def call_provider(self, provider_name, task):
        key = self.config.get(f"{provider_name.lower()}_api_key", "FREE_ACCESS" if provider_name in ["Puter", "ApiFreeLLM", "Zai"] else "MOCK_KEY")

        provider_info = {
            "Puter": "User-Pays model (No setup required)",
            "ApiFreeLLM": "Free 200B+ models (Small delay between requests)",
            "JulesAPI": "Optimized developer interface",
            "Routeway": "Unlimited GLM-4.6 access",
            "Zai": "GLM-4.7 Anthropic-compatible free endpoint",
            "Gemini": "Google AI Studio free access"
        }

        info = provider_info.get(provider_name, "Standard API provider")
        return f"RESPONSE from {provider_name} ({info}): Processed task: {task}"
