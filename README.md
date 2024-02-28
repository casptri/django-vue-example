[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# django-vue-example
## About The Project
An example project for a django-vue application as back and front end.
Django in conjunction with django-ninja and all the power of python for the backend api.
Vue3 with quasar for the frontend.
Furthermore deployment for kubernetes and for development purposes also docker compose files are included.

## Getting Started
Different ways to run the app are provided.
### Prerequisites

#### Local
At least python3.10, pip and poetry are necessary.

#### Docker Compose
Docker and docker compose

#### Kubernetes
A running kubernetes instance. The app is developed on a k8s instance.
Furthermore a docker registry needs to be avaiable.

### Installation
#### Local
#### Docker Compose
#### Kubernetes

## Usage
#### Local
```
poetry shell
djm runserver 8881
```
#### Docker Compose
```
docker-compose build
docker-compose up
```
#### Kubernetes
```
docker build . -f Dockerfile -t localhost:32000/dveapi:latest
docker push localhost:32000/avgwebapi:latest
docker build . -f static.Dockerfile -t localhost:32000/dveapi-static:latest
docker push localhost:32000/dveapi-static:latest

helm upgrade foody-floppy dveChart
```

## Roadmap
- Django API
    - Basic
        - [x] django setup
        - [x] Dockerfile
        - [ ] db setup
            - [ ] django settings
            - [ ] setup postgres
                - [ ] compose
                - [ ] helm
        - [ ] static files
            - [ ] django settings
            - [ ] serve static files with nginx
                - [x] compose
                - [ ] helm
    - Authentication
        - [ ] create api
    - File Share API
        - [x] create api
        - [ ] upload
        - [ ] download
        - [ ] serve files with nginx autoindex
            - [ ] compose
            - [ ] helm
- Vue3 App
    - Basic
        - [x] quasar setup
        - [ ] Dockerfile
        - [ ] compose
        - [ ] helm
- Helm additionals
    - [ ] Ingress
    - [ ] HPA
- [ ] Fill out Readme

## Contributing

## License

## Contact

## Acknowledgments

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/casptri/django-vue-example.svg?style=for-the-badge
[contributors-url]: https://github.com/casptri/django-vue-example/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/casptri/django-vue-example.svg?style=for-the-badge
[forks-url]: https://github.com/casptri/django-vue-example/network/members
[stars-shield]: https://img.shields.io/github/stars/casptri/django-vue-example.svg?style=for-the-badge
[stars-url]: https://github.com/casptri/django-vue-example/stargazers
[issues-shield]: https://img.shields.io/github/issues/casptri/django-vue-example.svg?style=for-the-badge
[issues-url]: https://github.com/casptri/django-vue-example/issues
[license-shield]: https://img.shields.io/github/license/casptri/django-vue-example.svg?style=for-the-badge
[license-url]: https://github.com/casptri/django-vue-example/blob/master/LICENSE.txt

