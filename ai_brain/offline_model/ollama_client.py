import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="gemma4"):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt, system=None):
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if system:
            payload["system"] = system

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "Error: No response from Ollama")
        except Exception as e:
            return f"Ollama Connection Error: {e}. Ensure Ollama is running with 'ollama serve'."

    def check_health(self):
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            return response.status_code == 200
        except:
            return False
