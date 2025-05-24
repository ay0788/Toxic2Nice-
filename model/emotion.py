from transformers import pipeline

# Load zero-shot classification model for emotion detection
emotion_model = pipeline("zero-shot-classification",
                         model="facebook/bart-large-mnli")

# Define candidate emotions
candidate_labels = ["joy", "anger", "sadness", "fear", "disgust", "surprise", "neutral"]

def detect_emotion(text):
    result = emotion_model(text, candidate_labels)
    top_emotion = result["labels"][0]
    score = result["scores"][0]
    return top_emotion, score
