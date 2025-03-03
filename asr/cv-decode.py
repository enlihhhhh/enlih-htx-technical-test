import pandas as pd
import numpy as np
import requests
from tqdm import tqdm
import os

# Declare the file paths required (change the paths as required)
audio_folder = "data/cv-valid-dev"
output_csv_path = "data/cv-valid-dev.csv"

# Get the list of all audio files in the folder (ensuring that they are .mp3 files)
audio_files = [file for file in os.listdir(audio_folder) if file.endswith(".mp3")]

# Sort the audio files by name
audio_files = sorted(audio_files)

audio_files = audio_files[:2]

# Initialise a Pandas Dataframe to store the transcribed results
df = pd.DataFrame({"filename": audio_files, "generated_text": pd.NA})

# Read cv-valid-dev.csv file
cv_valid_dev_df = pd.read_csv(output_csv_path)

# FastAPI endpoint
api_url = "http://localhost:8001/asr"

# Iterate through the audio files in the folder
for index, row in tqdm(df.iterrows(), total=len(df), desc="Processing audio files"):
    audio_file = os.path.join(audio_folder, row["filename"])

    try:
        # Send a POST request to the FastAPI endpoint
        response = requests.post(api_url, files={"file": open(audio_file, "rb")})

        if response.status_code == 200:
            # Extract the transcription and duration from the response
            transcription = response.json()["transcription"]
            duration = response.json()["duration"]

            # Append the results to the Pandas Dataframe
            df.loc[index, "generated_text"] = transcription
        else:
            print(f"Error processing {audio_file}: {response.status_code}")
    except Exception as e:
        print(f"Failed to process {audio_file}: {str(e)}")

# Append the transcribed results to the original cv-valid-dev.csv file
cv_valid_dev_df['generated_text'] = df['generated_text'].str.lower()

# Save the results to the output CSV file
try:
    cv_valid_dev_df.to_csv(output_csv_path, index=False)
    print(f"Transcriptions saved to {output_csv_path}")
except Exception as e:
    print(f"Failed to save transcriptions to {output_csv_path}: {str(e)}")