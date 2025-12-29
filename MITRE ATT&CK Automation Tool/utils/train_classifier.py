from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Training data (example TTP sentences)
X_train = [
    "powershell used to download malicious payload",
    "registry run key used for persistence",
    "credential dumping by accessing lsass memory"
]

# Corresponding MITRE technique labels
y_train = [
    "T1059",  # Command and Scripting Interpreter
    "T1547",  # Boot or Logon Autostart Execution
    "T1003"   # Credential Dumping
]

# Vectorization
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X_train)

# Train classifier
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y_train)

# Save trained model
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ MITRE ATT&CK classifier trained and saved")
