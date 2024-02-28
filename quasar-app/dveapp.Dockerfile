ARG NODE_VERSION=18

FROM node:${NODE_VERSION}-alpine AS builder

ENV DockerHome=/home/app/webapp
RUN mkdir -p $DockerHome
WORKDIR $DockerHome

COPY dveApp/ ./

RUN npm install

RUN npm run build

FROM nginx:1.25.3-alpine as base

COPY --from=builder /home/app/webapp/dist/spa /usr/share/nginx/html

EXPOSE 80


