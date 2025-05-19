from transformers import BertTokenizer, BertForSequenceClassification
import torch

class Classifier:
    def __init__(self, model_name='bert-base-uncased', num_labels=5):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return probs.detach().numpy()
