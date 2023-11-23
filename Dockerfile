FROM python:3.7-alpine
EXPOSE 8081
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add musl-dev libpq-dev gcc
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
#ENTRYPOINT ["python3"]

CMD ["/bin/sh", "-c", "python3 tues_db/manage.py makemigrations && python3 tues_db/manage.py migrate && python3 tues_db/manage.py runserver 0.0.0.0:8081"]
