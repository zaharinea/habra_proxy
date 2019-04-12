FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk upgrade && \
    apk add --no-cache build-base gcc python3-dev && \
    rm -rf /var/cache/apk/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . /app

EXPOSE 8000
CMD ["python", "app.py"]
