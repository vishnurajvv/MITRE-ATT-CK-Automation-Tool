import pickle

# Load trained model and vectorizer
with open("model/model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def predict_technique(sentence: str) -> str:
    """
    Predicts MITRE ATT&CK Technique ID for a given sentence
    """
    vector = vectorizer.transform([sentence])
    return model.predict(vector)[0]
