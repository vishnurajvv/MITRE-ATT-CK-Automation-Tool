from fastapi import FastAPI
from preprocessing.clean_text import clean_text
from preprocessing.extract_text import extract_attack_sentences
from model.predict_ttp import predict_technique
from mapping.mitre_mapper import map_technique

app = FastAPI(
    title="MITRE ATT&CK Automation Tool",
    description="AI-based TTP extraction and MITRE ATT&CK classification",
    version="1.0"
)

@app.post("/analyze")
def analyze_report(report: str):
    """
    Accepts a threat report as input and returns
    MITRE ATT&CK mapped TTPs
    """
    cleaned_report = clean_text(report)
    ttp_sentences = extract_attack_sentences(cleaned_report)

    results = []
    for sentence in ttp_sentences:
        technique_id = predict_technique(sentence)
        results.append({
            "sentence": sentence,
            "technique_id": technique_id,
            "technique_name": map_technique(technique_id)
        })

    return results
