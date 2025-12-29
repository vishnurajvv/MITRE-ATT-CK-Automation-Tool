import json

def load_mitre_data(path="data/mitre_attack.json"):
    """
    Loads MITRE ATT&CK techniques from a STIX-like JSON file
    and returns a dictionary:
    { "T1059": "Command and Scripting Interpreter", ... }
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    techniques = {}

    for obj in data.get("objects", []):
        if obj.get("type") == "attack-pattern":
            for ref in obj.get("external_references", []):
                if ref.get("source_name") == "mitre-attack":
                    techniques[ref.get("external_id")] = obj.get("name")

    return techniques
