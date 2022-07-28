FROM python:3.8-slim
WORKDIR /home/juan/
COPY dev_requirements.txt ./
COPY requirements.txt ./
RUN python3 -m pip install -r dev_requirements.txt # requirements are installed first because is less probably changed
RUN python3 -m pip install -r requirements.txt
COPY ./camera_simulator/ ./camera_simulator/
COPY ./tests/ ./tests/
ENTRYPOINT pytest tests/ .
