import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = {
    "src_port": [80, 443, 22, 445, 3389, 53],
    "dst_port": [1024, 5566, 8090, 33445, 9000, 1200],
    "packet_size": [400, 800, 150, 2000, 300, 100],
    "malicious": [0, 0, 1, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df.drop("malicious", axis=1)
y = df["malicious"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("model.pkl created successfully!")
