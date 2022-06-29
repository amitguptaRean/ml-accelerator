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
There are two ways to run the data preparation and model training code - Azure DevOps Pipeline(for production release engineers and Devvops engineers) and run/debug/develop the code locally(for Data Scientists).

## Azure DevOps Pipeline for Release and DevOps Engineers
To trigger a new model build, go to Pipelines section in Azure DevOps and trigger the [`Batch AI AML` pipeline](https://dev.azure.com/PPGit/Digital%20Data%20Science/_build?definitionId=1397) based off the branch you are working off. 

Note that any code update to `develop` or `main` branch will automatically trigger a new build.

## The code for the aforementioned pipeline is stored at `$.pipelines/batch_ai-dataprep.yml`.

The pipeline stages are summarized below:


#### Model CI

- Linting (code quality analysis) (Coming Soon)
- Unit tests and code coverage analysis (Coming Soon)
- Build and publish _ML Training Pipeline_ in an _ML Workspace_. The code for this is stored at `$.ml_service/pipelines/batchai_training_pipeline.py`

#### Train model

- Determine the ID of the _ML Training Pipeline_ published in the previous stage.
- Trigger the _ML Training Pipeline_ and waits for it to complete.
  - This is an **agentless** job. The CI pipeline can wait for ML pipeline completion for hours or even days without using agent resources. The code for this is stored at `$.ml_service/pipelines/run_train_pipeline.py`.
- Determine if a new model was registered by the _ML Training Pipeline_. (Coming Soon)
  - If the model evaluation step of the AML Pipeline determines that the new model doesn't perform any better than the previous one, the new model won't register and the _ML Training Pipeline_ will be **canceled**. In this case, you'll see a message in the 'Train Model' job under the 'Determine if evaluation succeeded and new model is registered' step saying '**Model was not registered for this run.**'
  - **Note**: *while it's possible to do an Evaluation Step as part of the ADO pipeline, this evaluation is logically part of the work done by Data Scientists, and as such the recommendation is that this step is done as part of the AML Pipeline and not ADO pipelines.*
- [Additional Variables and Configuration](#additional-variables-and-configuration) for configuring this and other behavior.

## Data Preparation

From the root of the repository, run the following command:
```
python tbd
```
The same script will be used by MLOps pipeline to download input files from workspace dataset and storing output files in dataset for the training job
## Training the model

From the root of the repository, run the following command:
```
python helloworld_training.py  
```

## Logging and Model metrics
During model training loggers and metrics are stored in https://ml.azure.com/experiments

## Development Setup for Data Scientists
All scripts should be runnable with the present working directory at the path of the workspace. (In the same folder as this README file) This ensures a common starting point regardless of environment (local, remote, Azure, MLOps, etc.) and more importantly, ensures developers can use an integrated development environment to debug and step through running code.

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

From the root of the repository, run the following command:
```
python .\src\data_preparation\batchai\batchai_datapreparation.py
or
Can execute through run button of the file.

In Data preparation, Input data is cloned form Azure blob storage and saved in DataPrep_inputs folder, these data files were preprocessed and stored in DataPrep_outputs folder for model training.
```

### Training the model 
You can copy already trained model from cloud to your local ./outputs or train the model on your local machine
From the root of the repository, run the following command:
```
python .\src\training\batchai\batchai_training.py
or
Can execute through run button of the file.

In Training, data is fetched from DataPrep_outputs based on location, and product_id based on these info it fetches data.csv and target.csv data files and starts modle building in subsequent steps. after successfull model building it generates coefficient.csv and rmse.csv files which were stored in Training_Output folder.
```

### Run Inference - Unit test on you development machine
From the root of the repository, run the following command:
```
python helloworld_inference.py
or
Can execute through run button of the file.
```

### Unit Tests
From the root of repository,
```
python -m unittest test.inference.batchai.batchai_inference_test.BatchaiInferencingTest.test_batchinference
python -m unittest test.training.batchai.batchai_training_test.TestTraining.test_training_dataloading

```


### Additional Variables and Configuration

#### More variable options

There are more variables used in the project. They're defined in one place: for local execution and for using Azure DevOps Pipelines.

For using Azure Pipelines, all variables are defined in `$.env` file. Using the default values as a starting point, adjust the variables to suit your requirements.
