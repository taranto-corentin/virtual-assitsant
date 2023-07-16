from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class Chatbot:
    def __init__(self):
        model_name = "gpt2"

        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def generate_response(self, text: str):
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)

        return self.tokenizer.decode(output[0], skip_special_token=True)

    def communicate(self, text: str):
        response = self.generate_response(text)
        print(response)
