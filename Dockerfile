FROM henriquegf12/raspberian-opencv4.x


#local da aplicacao
WORKDIR /usr/src/app
RUN sudo apt-get install v4l-utils -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]