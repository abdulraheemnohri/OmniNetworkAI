from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class OfflineAIBrain:
    def __init__(self, model_name="Qwen/Qwen2.5-1.5B"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")

    def process_command(self, command):
        inputs = self.tokenizer(command, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**inputs, max_new_tokens=512)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response