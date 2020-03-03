FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


# Server
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8081"]