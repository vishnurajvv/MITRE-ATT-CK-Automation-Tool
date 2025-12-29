import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Common attack-related keywords
KEYWORDS = [
    "powershell",
    "registry",
    "credential",
    "lsass",
    "dump",
    "persistence",
    "execute",
    "payload"
]

def extract_attack_sentences(text: str):
    """
    Extracts sentences likely describing attacker behavior (TTPs)
    """
    doc = nlp(text)
    attack_sentences = []

    for sent in doc.sents:
        if any(keyword in sent.text.lower() for keyword in KEYWORDS):
            attack_sentences.append(sent.text.strip())

    return attack_sentences
