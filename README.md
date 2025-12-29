MITRE ATT&CK Automation Tool

An AI-powered cybersecurity automation tool that extracts adversary Tactics, Techniques, and Procedures (TTPs) from unstructured threat intelligence reports and automatically maps them to **MITRE ATT&CK** techniques — eliminating the need for manual human expert analysis.



 Project Overview

Security teams spend significant time manually analyzing threat reports and mapping attacker behavior to MITRE ATT&CK.  
This project automates that process using **Natural Language Processing (NLP)** and **Machine Learning (ML)**.

The tool:
- Reads raw threat intelligence text
- Identifies attacker behavior sentences (TTPs)
- Classifies them into MITRE ATT&CK Technique IDs (Txxxx)
- Returns structured, SOC-ready output



 Key Features

-  Automatic TTP sentence extraction using NLP
-  Machine Learning-based MITRE ATT&CK classification
-  MITRE ATT&CK STIX-style dataset support
-  FastAPI backend for automation
-  Modular, industry-grade project structure
-  No human expert intervention required



 Project Structure

 mitre_attack_automation/
 
├── data/

│ ├── mitre_attack.json

│ └── sample_reports/

│ └── apt_report.txt

├── preprocessing/

│ ├── clean_text.py

│ └── extract_text.py

├── utils/

│ └── load_mitre.py

├── model/

│ ├── train_classifier.py

│ └── predict_ttp.py

├── mapping/

│ └── mitre_mapper.py

├── api/

│ └── main.py

├── requirements.txt

└── README.md



 Tech Stack

- **Language:** Python  
- **NLP:** spaCy  
- **Machine Learning:** scikit-learn  
- **Backend API:** FastAPI  
- **Threat Framework:** MITRE ATT&CK  
- **Model Type:** TF-IDF + Logistic Regression  



 How It Works

1. Input a threat report (text)
2. Clean and preprocess the text
3. Extract attack-related sentences
4. Classify each sentence into a MITRE ATT&CK technique
5. Map Technique ID → Technique name
6. Return structured output (JSON)



 Installation

### Clone the repository
```bash
git clone https://github.com/vishnurajvv/MITRE-ATT-CK-Automation-Tool.git
cd mitre-attack-automation
