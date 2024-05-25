
FROM python:3.10
WORKDIR /app
COPY . /app

RUN apt update -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python", "app.py"]