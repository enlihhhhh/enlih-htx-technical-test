# ASR API 

This README provides information on how to run the Automatic Speech Recognition (ASR) API using the `wav2vec2-large-960h` model.

## Pre-requisites 
- You will need to have an ubuntu system (preferably) with docker and docker compose installed by running the following command
```bash
sudo snap install docker
```
- Preferably using Visual Studio Code to run all the code in this package

## Directory Structure

- `app/data/`: Contains audio files and metadata.
- `asr_api.py`: Implements the ASR API using FastAPI.
- `cv-decode.py`: Processes audio files using the ASR API and saves transcriptions to the original cv-valid-dev.csv.
- `Dockerfile`: Defines how the ASR API is containerised in Docker.
- `docker-compose.yaml`: Defines the asr-api service and ensures the container is built and run.
- `requirements.txt`: Lists Python dependencies for the ASR API.

## How to Run ASR-API

### Testing ASR API locally without Docker

Ensure that you have already set up Python in your environment by following the instructions in the main README.md file in the directory ```enlih-htx-technical-test/README.md```

Use the following curl commands to start the ASR API accordingly
```bash
# Starts the ASR_API
uvicorn asr_api:app --host 0.0.0.0 --port 8001 

# Service working if "pong" returned
curl http://localhost:8001/ping 

# Example usage to test sample audio file 
curl -F 'file=@path/to/folder/enlih-htx-technical-test/asr/data/cv-valid-dev/sample-000000.mp3' http://localhost:8001/asr
```

### Tesing ASR API with Docker

**1. Build and start the Docker container:**
```bash
docker-compose up --build # build docker container
docker-compose restart # restarts the docker container
docker-compose down # stops the docker container
```
After running ```docker-compose up --build```, you should see the following information in your terminal
```bash
[+] Running 3/3
 ✔ asr-api              Built                                                                                                          0.0s 
 ✔ Network asr_default  Created                                                                                                        0.1s 
 ✔ Container asr-api    Created                                                                                                        0.0s 
Attaching to asr-api
asr-api  | Some weights of Wav2Vec2ForCTC were not initialized from the model checkpoint at facebook/wav2vec2-large-960h and are newly initialized: ['wav2vec2.masked_spec_embed']
asr-api  | You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
asr-api  | INFO:     Started server process [1]
asr-api  | INFO:     Waiting for application startup.
asr-api  | INFO:     Application startup complete.
asr-api  | INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
asr-api  | INFO:     172.19.0.1:59848 - "POST /asr HTTP/1.1" 200 OK
asr-api  | INFO:     172.19.0.1:51260 - "GET /ping HTTP/1.1" 200 OK
```
If you see the following information, the ASR-API has started and you can test the following code to see if it connects to the API


```bash
# Service working if "pong" returned
curl http://localhost:8001/ping 

# Example usage to test sample audio file 
curl -F 'file=@path/to/folder/enlih-htx-technical-test/asr/data/cv-valid-dev/sample-000000.mp3' http://localhost:8001/asr
```

## How to run cv-decode.py

- Ensure that you are in the correct directory by using ```cd ./asr``` to navigate into the asr folder. 
- Then run the following command to add the transcribed results inside the original cv-valid-dev with the column name ```generated_text```

```bash
python cv-decode.py
```

```Note: The current file inside data/cv-valid-dev.csv has the transcribed result inside, if you wish to replicate the process, delete the current file and replace it with the original cv-valid-dev.csv from the common_voice folder.```