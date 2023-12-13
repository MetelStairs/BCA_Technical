FROM python:3.11.7-slim

WORKDIR /usr/src/app

COPY requirements.txt .

COPY . .

CMD ["python", "hailstone.py"]