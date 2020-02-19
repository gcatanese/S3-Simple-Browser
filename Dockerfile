FROM python:3

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]