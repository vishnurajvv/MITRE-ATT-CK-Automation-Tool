import re

def clean_text(text: str) -> str:
    """
    Cleans raw threat report text for NLP processing
    """
    text = text.lower()
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()
