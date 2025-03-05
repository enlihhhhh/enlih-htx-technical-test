# Detecting Hot Words

This README provides information on how to run the code to detect hot words in Task 5.

## Pre-requisites 

Ensure that you have a virtual environment with `requirements.txt` installed.

## Directory Structure

- `cv-hotword-5a.ipynb`: Notebook to find the audio files that contains the hotwords
- `cv-hotword-similarity-5b.ipynb:` Notebook to get similar phrase to the hotwords from the transcribed resuls from my fine-tuned model
- `cv-valid-dev.csv`: Contains the transcribed results from my fine-tuned model and the similarity scores for task 5b
- `detected.txt`: text files which contains the list of mp3 filenames for task 5a

Note: Ensure that you have the audio folder data inside the `asr folder` before running the code here as this task will be reusing the audio in that folder so there is no need to copy paste the folder twice

 transcriptions using the fine-tuned `enlihhhhh/wav2vec2-large-960h-cv` model
- `vocab.json`: JSON file containing the vocabulary of the Common Voice dataset

Note: For the data folder, I have uploaded the CSV files for data reading, however you have to download the audio folders `cv-valid-test and cv-valid-train` and place them inside the `data/` folder

## How to Run Code

Navigate to each individual notebook and run the code accordingly per cell