## Test container setup for gpu-enabled mmyolo

Set up `Dockerfile`, `docker-compose.yml` and additional requirements `requirements.txt`.  
These will be used for devcontainer. 

Note: While this container set up is based on the Dockerfile in [original repository](https://github.com/AILab-CVC/YOLO-World) I had to do some version-matching to make things work. 

### Test container 
```bash
cd .devcontainer

docker compose up -d #--force-recreate

docker exec -it asn-yolo-container /bin/bash
```