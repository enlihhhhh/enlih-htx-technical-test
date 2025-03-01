# Using the slim variant of Python 3.11 image to minimise the image size
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

# Copy the API application code into the container
COPY asr_api.py .

# Expose the API port
EXPOSE 8001

# Command Line to run the API
CMD ["uvicorn", "asr_api:app", "--host", "0.0.0.0", "--port", "8001"]
