FROM python:3.9.16-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./docker/web/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

EXPOSE 8000

COPY . .
RUN pip install -r requirements.txt