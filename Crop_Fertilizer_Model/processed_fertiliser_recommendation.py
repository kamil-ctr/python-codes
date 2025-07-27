import pandas as pd
from sklearn.preprocessing import LabelEncoder

raw_data_path = "/Users/mohammadkamilkhan/Desktop/Fertilizer.csv"
data = pd.read_csv(raw_data_path)

data = data.drop(columns=["Unnamed: 0"])

label_encoder = LabelEncoder()
data["Crop"] = label_encoder.fit_transform(data["Crop"])

processed_data_path = "/Users/mohammadkamilkhan/Desktop/Processed_FertilizerData.csv"
data.to_csv(processed_data_path, index=False)

print(f"Processed data saved to: {processed_data_path}")
