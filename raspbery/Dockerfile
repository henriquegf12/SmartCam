FROM henriquegf12/identify_raspberry_cam:latest
WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "main.py"]