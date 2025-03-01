# En Lih's HTX Technical Test Submission

## **Repository Directories**
- ```asr:``` Folder containing code for Task 2 to create asr-API
- ```asr-train:```
- ```essay-ssl.pdf:``` Essay for proposing model self-supervised learning pipeline
- ```hotword-detection:```
- ```training-report.pdf:``` Training Report to compare results from task 2a for the ```cv-valid-dev``` dataset

```Note: For asr, asr-train, and hotword-detection folders, each of them will contain their respective README.md files for information on how to run the code inside```
---

## **Local Environment Setup Instructions**

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.9 or higher
- Conda or Miniconda for virtual environment management

### **Instructions to install Miniconda with Python on your system**

### For Linux (Preferred)
```bash
# Download Miniconda Installer For Linux (Ubuntu/Debian, Fedora, Arch)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Run the installer
bash ~/Miniconda3-latest-Linux-x86_64.sh

# Close and reopen your terminal, then run the following code to activate Miniconda
source ~/.bashrc

# Verify Installation of Miniconda
conda --version
```

For Windows and macOS installation, kindly refer to the following [Official Anconda Website](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-linux-installation) for more information on the installation

---


### **1. Create a Virtual Environment**
Use Conda or Miniconda to create and activate a virtual environment (downgrade or upgrade Python Version when necessary):

### **Using Conda (Preferred)**
```bash
# Creating virtual environment
conda create --name htx_env python=3.11

# Activating environment
conda activate htx_env

# Deactivate environment
conda deactivate htx_env
```

### **Using Python's venv**
```bash
# Creating virtual environment
python -m venv htx_env

"""
Steps on Virtual Environment management
""" 
htx_env\Scripts\activate # Activate env on Windows
source htx_env/bin/activate # Activate env on macOS / Linus

# Deactivate environment
deactivate
```
---

### **2. Install Required Libraries**
Install all required libraries using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```

```Note: this set-up is only for running code locally on your machine, the tasks using Docker to run has their own seperate instructions```

