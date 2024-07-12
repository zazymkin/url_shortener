FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY src/ /app

WORKDIR /app

CMD ["python",  "main.py"]
