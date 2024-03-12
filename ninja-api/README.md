helm install --debug --dry-run fatty-feasty ./dveapiChart/

docker build -t dveapi:0.1.0 -f dveapi.Dockerfile .
docker build -t dveapi-static:0.1.0 --build-arg API_VERSION=0.1.0 --build-arg API_NAME=dveapi -f static.Dockerfile .
