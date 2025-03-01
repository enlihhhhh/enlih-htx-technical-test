from fastapi import FastAPI, File, UploadFile, HTTPException
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf
import torch
import librosa
import numpy as np
import os

# Initialise FastAPI
app = FastAPI()

# Load the model
MODEL_NAME = os.getenv("MODEL_NAME", "facebook/wav2vec2-large-960h")
processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_NAME)

@app.get("/ping")
def ping():
    return {"response": "pong"}

@app.post("/asr")
async def asr(file: UploadFile = File(...)):

    try:
        # Read the audio file
        audio, sample_rate = sf.read(file.file)

        if sample_rate != 16000:
            audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=16000)
        
        # Perform preprocessing of audio
        input_values = processor(audio, return_tensors="pt", sampling_rate=16000).input_values

        # Perform inference
        with torch.no_grad():
            logits = model(input_values).logits

        # Decode the logits 
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.decode(predicted_ids[0]) 

        # Get the total duration of the processing of audio file
        duration = len(audio) / 16000

        # Explicitly close the file to ensure resources are released
        file.file.close()

        return {"transcription": str(transcription), "duration": str(duration)} # str() used to convert to strings
    
    except Exception as e:

        # Do not delete the file as the file is not processed
        raise HTTPException(status_code=500, detail=str(e))
