from huggingface_hub import hf_hub_download
import os

# Define the model repository and filename
repo_id = "wondervictor/YOLO-World"
filename = "yolo_world_v2_x_obj365v1_goldg_cc3mlite_pretrain_1280ft-14996a36.pth"

# Download the file
dir_path = '/workspaces/YOLO-World/weights' #os.path.dirname(os.path.realpath(__file__))
file_path = hf_hub_download(repo_id=repo_id, filename=filename, local_dir=dir_path)

print(f"Model weights saved to: {file_path}")

"""
# wget can be used to download files as well
wget -P weights/ https://huggingface.co/wondervictor/YOLO-World/resolve/main/yolo_world_v2_l_obj365v1_goldg_pretrain_1280ft-9babe3f6.pth
wget https://media.roboflow.com/notebooks/examples/dog.jpeg

# or use curl
WEIGHT="yolo_world_l_clip_base_dual_vlpan_2e-3adamw_32xb16_100e_o365_goldg_train_pretrained-0e566235.pth" curl -o weights/$WEIGHT -L https://huggingface.co/wondervictor/YOLO-World/resolve/main/$WEIGHT

"""