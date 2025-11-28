import pandas as pd
import joblib
import os

INPUT_DIR = "/input/logs"
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "alerts.csv")

model = joblib.load("model.pkl")

alerts = []

for file in os.listdir(INPUT_DIR):
    if file.endswith(".csv") or file.endswith(".log"):
        path = os.path.join(INPUT_DIR, file)
        
        try:
            df = pd.read_csv(path)
            predictions = model.predict(df)
            df["prediction"] = predictions
            df["file"] = file
            alerts.append(df)
        except Exception as e:
            print(f"Error processing {file}: {e}")

if alerts:
    final_df = pd.concat(alerts)
    final_df.to_csv(OUTPUT_FILE, index=False)
    print("Alerts saved to /output/alerts.csv")
else:
    print("No logs found or no alerts generated.")
