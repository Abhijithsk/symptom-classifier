# 🩺 Symptom Classifier — Clinical AI API

A production-grade **disease prediction system** built with PyTorch, served via FastAPI, containerised with Docker, and validated through a GitHub Actions CI/CD pipeline.

> Built as part of a MedTech AI portfolio targeting clinical decision support systems.

---

## 🏗️ Architecture

```
User Input (symptoms text)
        │
        ▼
┌─────────────────────┐
│   FastAPI Server    │  POST /predict
│   (uvicorn)         │  GET  /health
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  PyTorch Model      │  Embedding → Linear → Softmax
│  SymptomClassifier  │  Trained on 4920 samples
└────────┬────────────┘
         │
         ▼
  { disease, confidence }
```

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Architecture | Embedding + 2-layer MLP |
| Training samples | 4,920 |
| Classes | 41 diseases |
| Final accuracy | **100%** (test set) |
| Inference latency | < 10ms |

---

## 🚀 Quick Start

### Option 1 — Docker (recommended)

```bash
docker pull ghcr.io/abhijithsk/symptom-classifier:latest
docker run -p 8000:8000 ghcr.io/abhijithsk/symptom-classifier:latest
```

### Option 2 — Local

<<<<<<< HEAD
=======
```bash# 🩺 Symptom Classifier — Clinical AI API

A production-grade **disease prediction system** built with PyTorch, served via FastAPI, containerised with Docker, and validated through a GitHub Actions CI/CD pipeline.

> Built as part of a MedTech AI portfolio targeting clinical decision support systems.

---

## 🏗️ Architecture

```
User Input (symptoms text)
        │
        ▼
┌─────────────────────┐
│   FastAPI Server    │  POST /predict
│   (uvicorn)         │  GET  /health
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  PyTorch Model      │  Embedding → Linear → Softmax
│  SymptomClassifier  │  Trained on 4920 samples
└────────┬────────────┘
         │
         ▼
  { disease, confidence }
```

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Architecture | Embedding + 2-layer MLP |
| Training samples | 4,920 |
| Classes | 41 diseases |
| Final accuracy | **100%** (test set) |
| Inference latency | < 10ms |

---

## 🚀 Quick Start

### Option 1 — Docker (recommended)

```bash
docker pull ghcr.io/abhijithsk/symptom-classifier:latest
docker run -p 8000:8000 ghcr.io/abhijithsk/symptom-classifier:latest
```

### Option 2 — Local

>>>>>>> dfa8c24db0ecd8a75339dbf16cca9d152423e404
```bash
git clone https://github.com/Abhijithsk/symptom-classifier.git
cd symptom-classifier

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
uvicorn api.main:app --reload
```

Open **http://127.0.0.1:8000/docs** for the interactive API explorer.

---

## 📡 API Reference

### `POST /predict`

Predict disease from symptom description.

**Request**
```json
{
  "symptoms": "fever headache chills body ache"
}
```

**Response**
```json
{
  "disease": "Malaria",
  "confidence": 0.9821
}
```

### `GET /health`

```json
{ "status": "ok" }
```

---

## 🗂️ Project Structure

```
symptom-classifier/
├── model/
│   ├── model.py          # PyTorch nn.Module — embedding + MLP
│   ├── dataset.py        # DataLoader, tokenizer, LabelEncoder
│   └── train.py          # Training loop with evaluation
├── api/
│   ├── main.py           # FastAPI app with lifespan model loading
│   ├── schemas.py        # Pydantic request/response models
│   ├── predictor.py      # Inference wrapper
│   ├── model.pt          # Saved model weights
│   ├── vocab.json        # Symptom vocabulary
│   └── labels.json       # Disease class labels
├── tests/
│   └── test_api.py       # pytest + httpx test suite
├── Dockerfile
├── .dockerignore
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD
└── requirements.txt
```

---

## 🔬 Model Details

The classifier uses a lightweight neural architecture designed for low-latency inference in clinical environments:

```python
SymptomClassifier(
  embedding:  Embedding(vocab_size, 64)   # symptom token embeddings
  fc1:        Linear(64 → 128)            # feature extraction
  relu:        ReLU()
  dropout:    Dropout(0.3)                # regularisation
  fc2:        Linear(128 → num_classes)   # disease classification
)
```

**Input:** Free-text symptom string (tokenised, padded to length 20)  
**Output:** Disease label + softmax confidence score

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

```
tests/test_api.py::test_health               PASSED
tests/test_api.py::test_predict_returns_disease  PASSED
tests/test_api.py::test_predict_empty_symptoms   PASSED
```

---

## 🐳 Docker

```bash
# Build
docker build -t symptom-classifier .

# Run
docker run -p 8000:8000 symptom-classifier

# Test it
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"symptoms": "fever headache chills"}'
```

---

## ⚙️ CI/CD Pipeline

Every push to `main` triggers:

1. **Test job** — installs dependencies, runs pytest
2. **Docker job** — builds image, runs smoke test against `/health`

[![CI Pipeline](https://github.com/Abhijithsk/symptom-classifier/actions/workflows/ci.yml/badge.svg)](https://github.com/Abhijithsk/symptom-classifier/actions/workflows/ci.yml)

---

## 🗺️ Roadmap

- [ ] Swap tokenizer with ClinicalBERT embeddings
- [ ] Add multi-label prediction (comorbidities)
- [ ] Integrate MIMIC-III for real clinical training data
- [ ] Add MLflow experiment tracking
- [ ] Deploy to GCP Cloud Run with auto-scaling
- [ ] Add Prometheus metrics endpoint

---

## 📚 Dataset

[Disease Symptom Prediction](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset) — 41 diseases, 4920 samples, 17 symptom features per record.

---

## 👤 Author

**Abhijith SK** — AI/ML Engineer  
IIT Palakkad ecosystem · Kerala, India  
Building production-grade clinical AI systems

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
<<<<<<< HEAD
=======

git clone https://github.com/Abhijithsk/symptom-classifier.git
cd symptom-classifier

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
uvicorn api.main:app --reload
```

Open **http://127.0.0.1:8000/docs** for the interactive API explorer.

---

## 📡 API Reference

### `POST /predict`

Predict disease from symptom description.

**Request**
```json
{
  "symptoms": "fever headache chills body ache"
}
```

**Response**
```json
{
  "disease": "Malaria",
  "confidence": 0.9821
}
```

### `GET /health`

```json
{ "status": "ok" }
```

---

## 🗂️ Project Structure

```
symptom-classifier/
├── model/
│   ├── model.py          # PyTorch nn.Module — embedding + MLP
│   ├── dataset.py        # DataLoader, tokenizer, LabelEncoder
│   └── train.py          # Training loop with evaluation
├── api/
│   ├── main.py           # FastAPI app with lifespan model loading
│   ├── schemas.py        # Pydantic request/response models
│   ├── predictor.py      # Inference wrapper
│   ├── model.pt          # Saved model weights
│   ├── vocab.json        # Symptom vocabulary
│   └── labels.json       # Disease class labels
├── tests/
│   └── test_api.py       # pytest + httpx test suite
├── Dockerfile
├── .dockerignore
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD
└── requirements.txt
```

---

## 🔬 Model Details

The classifier uses a lightweight neural architecture designed for low-latency inference in clinical environments:

```python
SymptomClassifier(
  embedding:  Embedding(vocab_size, 64)   # symptom token embeddings
  fc1:        Linear(64 → 128)            # feature extraction
  relu:        ReLU()
  dropout:    Dropout(0.3)                # regularisation
  fc2:        Linear(128 → num_classes)   # disease classification
)
```

**Input:** Free-text symptom string (tokenised, padded to length 20)  
**Output:** Disease label + softmax confidence score

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

```
tests/test_api.py::test_health               PASSED
tests/test_api.py::test_predict_returns_disease  PASSED
tests/test_api.py::test_predict_empty_symptoms   PASSED
```

---

## 🐳 Docker

```bash
# Build
docker build -t symptom-classifier .

# Run
docker run -p 8000:8000 symptom-classifier

# Test it
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"symptoms": "fever headache chills"}'
```

---

## ⚙️ CI/CD Pipeline

Every push to `main` triggers:

1. **Test job** — installs dependencies, runs pytest
2. **Docker job** — builds image, runs smoke test against `/health`

[![CI Pipeline](https://github.com/Abhijithsk/symptom-classifier/actions/workflows/ci.yml/badge.svg)](https://github.com/Abhijithsk/symptom-classifier/actions/workflows/ci.yml)

---

## 🗺️ Roadmap

- [ ] Swap tokenizer with ClinicalBERT embeddings
- [ ] Add multi-label prediction (comorbidities)
- [ ] Integrate MIMIC-III for real clinical training data
- [ ] Add MLflow experiment tracking
- [ ] Deploy to GCP Cloud Run with auto-scaling
- [ ] Add Prometheus metrics endpoint

---

## 📚 Dataset

[Disease Symptom Prediction](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset) — 41 diseases, 4920 samples, 17 symptom features per record.

---

## 👤 Author

**Abhijith SK** — AI/ML Engineer  
IIT Palakkad ecosystem · Kerala, India  
Building production-grade clinical AI systems

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
[README (1).md](https://github.com/user-attachments/files/28661304/README.1.md)
>>>>>>> dfa8c24db0ecd8a75339dbf16cca9d152423e404
