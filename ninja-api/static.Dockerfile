ARG API_VERSION=latest
ARG API_NAME=dveapi
FROM ${API_NAME}:${API_VERSION} as api
#FROM localhost:32000/dveapi:latest as api

ENV DJANGO_STATIC_ROOT "/var/www/static/"

RUN djm collectstatic --noinput

FROM nginx

RUN mkdir -p /var/www/data/static
RUN mkdir -p /var/www/data/storage

COPY --from=api /var/www/static /var/www/data/static

COPY ./static.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
