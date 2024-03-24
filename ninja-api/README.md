# Install
## 
helm install --debug --dry-run doopy-dotty ./dveapiChart/
helm install doopy-dotty ./dveapiChart/
helm upgrade doopy-dotty ./dveapiChart/

docker build -t localhost:32000/dveapi:0.1.0 -f dveapi.Dockerfile .
docker build -t localhost:32000/dveapi-static:0.1.0 --build-arg API_VERSION=0.1.0 --build-arg API_NAME=localhost:32000/dveapi -f static.Dockerfile .

docker push localhost:32000/dveapi:0.1.0
docker push localhost:32000/dveapi-static:0.1.0

## With volume creation
```
helm install dveapi dveapiChart -f localStorage.yaml
```

