FROM python:3.8-slim-buster
MKDIR /opt/ml/ml-accelerator
COPY data/ /opt/ml/ml-accelerator/data
COPY model/ /opt/ml/ml-accelerator/model
COPY src/ /opt/ml/ml-accelerator/src
COPY test/ /opt/ml/ml-accelerator/test

WORKDIR /opt/ml/ml-accelerator
COPY .env .env
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python", "-u", "src/helloworld_training.py"]