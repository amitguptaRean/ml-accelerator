FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./src /src
WORKDIR  /src
CMD ["python", "-u", "helloworld_training.py"]