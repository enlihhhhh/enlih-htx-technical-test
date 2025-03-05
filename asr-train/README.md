# Fine-tuning ASR AI Model

This README provides information on how to run the code to fine-tune `facebook/wav2vec2-large-960h` model.

## Pre-requisites 

Ensure that you have a virtual environment with `requirements.txt` installed.

## Directory Structure

- `data/`: Contains audio files and metadata.
- `cv-train-2a.ipynb`: Contains Notebook to run the entire fine-tuning pipeline
- `cv-valid-dev.csv`: Contains transcriptions using the original `facebook/wav2vec2-large-960h` model
- `cv-valid-test.csv`: Contains transcriptions using the fine-tuned `enlihhhhh/wav2vec2-large-960h-cv` model
- `vocab.json`: JSON file containing the vocabulary of the Common Voice dataset

Note: For the data folder, I have uploaded the CSV files for data reading, however you have to download the audio folders `cv-valid-test and cv-valid-train` and place them inside the `data/` folder

## How to Run Code

Navigate to `cv-train-2a.ipynb` and follow the instructions inside the notebook cell by cell to run and retrieve the output

The code includes saving the fine-tuned model into HuggingFace Hub which is under the repository name `enlihhhhh/wav2vec2-large-960h-cv`.

Link to HuggingFace Repository Hub is [here](https://huggingface.co/enlihhhhh/wav2vec2-large-960h-cv
)