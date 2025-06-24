# Toxic2Nice: Detox Your Words with AI

![Toxic2Nice Banner]([https://github.com/ay0788/Toxic2Nice-/blob/main/toxic2nice.png])

**Toxic2Nice** is an AI-powered web application that detects toxic language in real-time and rephrases it into a more polite, respectful, and constructive version — all while preserving the intended message. It helps foster healthier digital communication by transforming negativity into empathy using the power of NLP.

---

## 🌟 Slogan

**"Toxic2Nice — Turning Harsh Words into Human Connection."**

---

## 🚀 Features

- 🔍 **Toxicity Detection** using fine-tuned transformer models (e.g., BERT, RoBERTa, or DistilBERT).
- ✨ **Polite Rewriting** with text generation or style transfer models.
- 🧠 Intelligent suggestions tailored to user input context.
- 🌐 User-friendly web interface for testing and live interaction.
- 📊 Analytics on toxicity levels for educational feedback.
- 🌍 Multilingual potential (roadmap feature).

---

## 🛠️ Technologies Used

| Layer         | Stack / Tools                             |
|---------------|--------------------------------------------|
| Frontend      | HTML, CSS,  |
| Backend       | Flask / FastAPI                            |
| NLP Models    | HuggingFace Transformers (e.g., BERT, GPT) |
| Toxicity Detection | Trained classifier using Jigsaw or Detoxify |
| Text Rewriting | Custom or pre-trained GPT-2 / T5          |

---

## 🧪 How It Works

1. **Input Phase**: User types a message.
2. **Toxicity Classification**: The system evaluates the input’s toxicity level (e.g., using a multi-label classifier).
3. **Rewriting Phase**: If toxic, the message is rewritten with polite alternatives while retaining meaning.
4. **Output Display**: Both the original and rephrased messages are displayed with toxicity score.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/toxic2nice.git
cd toxic2nice

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
