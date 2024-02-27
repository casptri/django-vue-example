FROM python:3.10-alpine
#FROM pypy:3.10-slim-bookworm
ENV DockerHome=/home/app/webapp
ENV AppName=dveApi

RUN mkdir -p $DockerHome
WORKDIR $DockerHome

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry

COPY dveapi/ ./dveapi
WORKDIR $DockerHome/$AppName

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

ENV DJANGO_DOCKER 1
ENV DJANGO_STATIC_ROOT "/var/www/static/"

EXPOSE 80

CMD djm migrate;uvicorn --host 0.0.0.0 --port 80 config.asgi:application


