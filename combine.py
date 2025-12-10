import os
import zipfile

import pandas as pd
from tqdm import tqdm
import requests

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

if not os.path.isdir("data"):
    os.makedirs("data")

month_dfs = []

for i in tqdm(range(1, 13), desc="Downloading and unzipping all Divvy .csv files."):
    i = "0" + str(i) if i < 10 else str(i)
    curr_zip_path = f"./data/2023{i}-divvy-tripdata.zip"
    download_path = f"https://divvy-tripdata.s3.amazonaws.com/2023{i}-divvy-tripdata.zip"

    download_file(download_path, curr_zip_path)

    with zipfile.ZipFile(f"./data/2023{i}-divvy-tripdata.zip", "r") as zip_file:
        zip_file.extractall("./data/divvy_month_data")
    
    os.remove(curr_zip_path)

for i in tqdm(range(1, 13), desc="Reading all Divvy .csv files."):
    i = "0" + str(i) if i < 10 else str(i)
    
    curr_df = pd.read_csv(f"./data/divvy_month_data/2023{i}-divvy-tripdata.csv")
    month_dfs.append(curr_df)

print("Creating concatenated .csv file.")

divvy_df = pd.concat(month_dfs, axis=0)
divvy_df.to_csv("./data/2023-divvy-tripdata.csv")

print("Successfully created merged .csv file. Path is ./data/2023-divvy-tripdata.csv")