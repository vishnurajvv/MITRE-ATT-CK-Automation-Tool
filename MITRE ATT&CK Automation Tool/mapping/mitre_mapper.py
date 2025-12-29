from utils.load_mitre import load_mitre_data

# Load MITRE ATT&CK techniques once
mitre_techniques = load_mitre_data()

def map_technique(technique_id: str) -> str:
    """
    Maps a MITRE Technique ID (Txxxx) to its technique name
    """
    return mitre_techniques.get(technique_id, "Unknown Technique")
