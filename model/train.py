import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
import json
from dataset import load_data, SymptomDataset
from model import SymptomClassifier

df, vocab, le = load_data("dataset.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["symptoms"].tolist(), df["label"].tolist(),
    test_size=0.2, random_state=42
)

train_ds = SymptomDataset(X_train, y_train, vocab)
test_ds  = SymptomDataset(X_test,  y_test,  vocab)

train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
test_loader  = DataLoader(test_ds,  batch_size=32)

vocab_size  = len(vocab) + 1
num_classes = len(le.classes_)
model = SymptomClassifier(vocab_size, num_classes)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(20):
    model.train()
    total_loss = 0
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        output = model(X_batch)
        loss = criterion(output, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    model.eval()
    correct = 0
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            preds = model(X_batch).argmax(dim=1)
            correct += (preds == y_batch).sum().item()

    acc = correct / len(test_ds) * 100
    print(f"Epoch {epoch+1:2d} | Loss: {total_loss:.3f} | Accuracy: {acc:.1f}%")

torch.save(model.state_dict(), "../api/model.pt")
with open("../api/vocab.json", "w") as f:
    json.dump(vocab, f)
with open("../api/labels.json", "w") as f:
    json.dump(le.classes_.tolist(), f)

print("Done! Saved model.pt, vocab.json, labels.json into api/")