FROM python:3.12.4-alpine

WORKDIR /app

COPY app .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python3", "main.py" ]