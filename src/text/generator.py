from transformers import pipeline

class TextGenerator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate(self, prompt, max_length=100):
        return self.generator(prompt, max_length=max_length, num_return_sequences=1)[0]['generated_text']