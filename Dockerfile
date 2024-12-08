FROM python:3.10.16-alpine3.20

EXPOSE 5000

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

copy app.py .

CMD [ "python", "app.py" ]