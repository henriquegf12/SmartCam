FROM balenalib/raspberrypi4-64-debian:latest
RUN sudo apt-get update
RUN sudo apt-get install v4l-utils
RUN sudo apt-get install python3
RUN sudo apt-get install python3-pip
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3","main.py"]

