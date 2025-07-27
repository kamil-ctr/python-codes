import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

raw_data_path = "/Users/mohammadkamilkhan/Desktop/MergeFileCrop.csv"
data = pd.read_csv(raw_data_path)

data = data.drop(columns=["Unnamed: 0"])

scaler = MinMaxScaler()
numerical_columns = ["temperature", "humidity", "ph", "rainfall"]
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

label_encoder = LabelEncoder()
data["label"] = label_encoder.fit_transform(data["label"])

processed_data_path = "/Users/mohammadkamilkhan/Desktop/Processed_MergeFileCrop.csv"
data.to_csv(processed_data_path, index=False)

print(f"Processed data saved to: {processed_data_path}")
