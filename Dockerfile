FROM python:3.8-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

ENV PYTHON_VERSION 3.8


CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
