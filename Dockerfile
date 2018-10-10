FROM python:3.7.0-alpine3.7

WORKDIR /app

COPY . /app

CMD ["python", "test.py"]