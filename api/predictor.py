import torch
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.model import SymptomClassifier

class Predictor:
    def __init__(self):
        base = os.path.dirname(__file__)
        with open(os.path.join(base, "vocab.json"))  as f: self.vocab  = json.load(f)
        with open(os.path.join(base, "labels.json")) as f: self.labels = json.load(f)

        vocab_size  = len(self.vocab) + 1
        num_classes = len(self.labels)

        self.model = SymptomClassifier(vocab_size, num_classes)
        self.model.load_state_dict(torch.load(
            os.path.join(base, "model.pt"), map_location="cpu"
        ))
        self.model.eval()

    def predict(self, symptoms: str):
        tokens = [self.vocab.get(w.strip(), 0) for w in symptoms.split()]
        tokens = tokens[:20] + [0] * (20 - len(tokens))
        x = torch.tensor([tokens], dtype=torch.long)

        with torch.no_grad():
            logits = self.model(x)
            probs  = torch.softmax(logits, dim=1)
            idx    = probs.argmax().item()

        return {
            "disease":    self.labels[idx],
            "confidence": round(float(probs[0][idx]), 4)
        }