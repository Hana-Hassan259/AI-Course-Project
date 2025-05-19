from transformers import pipeline

class ContentGenerator:
    def __init__(self, model_name='gpt2'):
        self.generator = pipeline('text-generation', model=model_name)

    def generate(self, prompt, max_length=100, temperature=0.7):
        return self.generator(prompt, max_length=max_length, temperature=temperature)
