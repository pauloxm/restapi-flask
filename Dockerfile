FROM python:3.10.12-alpine3.18

EXPOSE 5000

WORKDIR /app
COPY requirements.txt /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev mariadb-client

RUN pip install -r requirements.txt

RUN apk del build-deps

COPY application application
COPY config.py .
COPY wsgi.py .

CMD [ "python", "wsgi.py" ]