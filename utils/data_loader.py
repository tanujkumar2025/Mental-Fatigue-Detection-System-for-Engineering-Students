import pandas as pd
import os
DATA_PATH = "dataset/raw_data/engineering_students_fatigue_300.csv"
def load_dataset():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    data = pd.read_csv(DATA_PATH)
    print("\nDataset Loaded Successfully\n")
    print("Shape:", data.shape)
    print(data.head())

    return data