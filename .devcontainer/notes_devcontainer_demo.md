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

## Yolo-World repository in dev container 
### Demo
1. Fork 
2. Add `devcontainer.json` devcontainer config to the origin repo. 
3. Clone the forked repo in devcontainer
4. For this yolo-world, there is a git submodule, we need to clone this as well.
```
git submodule init 
git submodule update
```
5. try running the demo (PYTHONPATH is set in Dockerfile). More info can be found in `demo/README.md`. For data prep, read `docs/data.md`
```
python demo/simple_demo.py
```

#### Troubleshooting 

##### Enable model download 
To run the demo, change config for huggingface so the model can be downloaded from huggingface. 
Or, I can later download these locally and map the folder to the container volume. 
```
# text_model_name = '../pretrained_models/clip-vit-base-patch32-projection'
text_model_name = 'openai/clip-vit-base-patch32'
```

##### How to download weights
See `asn-learn/asn_download_weights.py`. Also, if running `simple_demo.py` for the first time, may need `lvis-api`.
```
pip install git+https://github.com/lvis-dataset/lvis-api.git
```

##### Gradio demo 
Need additional modules for gradio. Devcontainer handles 'port forwading' beautifully :) 
```
pip install -r requirements/demo_requirements.txt
pip install -r requirements/onyx_requirements.txt

python demo/gradio_demo.py ./configs/pretrain/yolo_world_v2_x_vlpan_bn_2e-3_100e_4x8gpus_obj365v1_goldg_train_1280ft_lvis_minival.py ./weights/yolo_world_v2_x_obj365v1_goldg_cc3mlite_pretrain_1280ft-14996a36.pth
```
