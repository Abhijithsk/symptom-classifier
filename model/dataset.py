import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset

def load_data(path="dataset.csv"):
    df = pd.read_csv(path)

    symptom_cols = [c for c in df.columns if "Symptom" in c]
    df[symptom_cols] = df[symptom_cols].fillna("")

    df["symptoms"] = df[symptom_cols].apply(
        lambda row: " ".join([s.strip() for s in row if s]), axis=1
    )

    all_words = set()
    for text in df["symptoms"]:
        all_words.update(text.split())
    vocab = {word: idx+1 for idx, word in enumerate(sorted(all_words))}
    vocab["<PAD>"] = 0

    le = LabelEncoder()
    df["label"] = le.fit_transform(df["Disease"])

    return df, vocab, le


class SymptomDataset(Dataset):
    def __init__(self, texts, labels, vocab, max_len=20):
        self.labels = labels
        self.max_len = max_len
        self.encoded = []
        for text in texts:
            tokens = [vocab.get(w, 0) for w in text.split()]
            tokens = tokens[:max_len] + [0] * (max_len - len(tokens))
            self.encoded.append(tokens)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        x = torch.tensor(self.encoded[idx], dtype=torch.long)
        y = torch.tensor(self.labels[idx], dtype=torch.long)
        return x, y