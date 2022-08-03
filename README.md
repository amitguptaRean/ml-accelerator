#Hello world model

ML acclerator models for various verticals

# Architecture

## Top Level Logical Architecture 

## Stack
The below dependencies should be installed using the requirements.txt file.  
pip install -r requirements.txt

| Component         | Ver           | Install   |
| ------------- | ------------- | ------------- |     
| sklearn |0.0 |  |
| scikit-learn | 1.0.1 |  |

# Run Steps
To run the data preparation and model training code: run/debug/develop the code locally(for Data Scientists).


Note that any code update to `develop` or `main` branch will automatically trigger a new build.


The pipeline stages are summarized below:


#### Model CI

- Linting (code quality analysis) (Coming Soon)
- Unit tests and code coverage analysis (Coming Soon)

## Training the model

From the root of the repository, run the following command:
```
python .\src\helloworld_training.py  
```


## Development Setup for Data Scientists
All scripts should be runnable with the present working directory at the path of the workspace. (In the same folder as this README file) This ensures a common starting point regardless of environment (local, remote, MLOps, etc.) and more importantly, ensures developers can use an integrated development environment to debug and step through running code.

### Prerequisites
Working within VS Code:
Ensure that python 3.10.4 is installed and selected as the default python interpreter

Clone the repo into a new workspace/folder.
Change the PWD to the workspace folder
Setup and activate the virtual python env
pip install from requirements.txt file

```
python --version
python -m venv .venv
 .venv\scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Now ensure that VS Code is using the python interpreter from the venv by checking the panel in the status bar. (e.g. "Python 3.8.10 64-bit ('.venv': venv)")
The .nev file has the AML_PIPELINE_EXEC_MODE setting that can be 
* 'PROD' : Run as pipeline
* 'DEV' : Run locally from develooper PC/VSCode

### Data Preparation
Data is given in the CardioGoodFitness.csv file


## Training the model
You can copy already trained model from cloud to your local ./outputs or train the model on your local machine
From the root of the repository, run the following command:
```
python .\src\helloworld_training.py 

```
Can execute through run button of the file.

After training, the subsequent model is serialized as a pickle (.pkl) file.

### Run Inference - Unit test on you development machine
From the root of the repository, run the following command:
```
python .\src\helloworld_inference.py 

```     
or
Can execute through run button of the file.

### Unit Tests
From the root of repository,
```                          
python -m unittest test.helloworld_inference_test
                             
```

# Docker image local build, and upload to AWS
```
(Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin 256555058276.dkr.ecr.us-east-2.amazonaws.com
docker build -t tcb-models .
docker tag tcb-models:latest 256555058276.dkr.ecr.us-east-2.amazonaws.com/tcb-models:latest
docker push 256555058276.dkr.ecr.us-east-2.amazonaws.com/tcb-models:latest

docker build --tag cardio-fitness-docker .
docker images
docker run -i -t ehm-efast-filemanager-py-docker
docker ps
docker stop <container id>
```