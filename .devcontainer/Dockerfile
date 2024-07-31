FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

ENV FORCE_CUDA="1"
ENV MMCV_WITH_OPS=1

FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

ENV PATH="/opt/conda/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip     \
    libgl1-mesa-glx \
    libsm6          \
    libxext6        \
    libxrender-dev  \
    libglib2.0-0    \
    git             \
    python3-dev     \
    python3-wheel

# Version info from https://pytorch.org/get-started/previous-versions/    
RUN pip3 install --no-cache-dir --index-url https://download.pytorch.org/whl/cu118 \
    wheel                   \
    "torch==2.0.1"          \
    "torchvision==0.15.2"   \
    "torchaudio==2.0.2"    

RUN pip3 install --upgrade pip \
    && pip3 install   \
        mmengine      \
        setuptools    \
        openmim       

# Install mmcv, mmdet, mmyolo 
RUN mim install "mmcv==2.0.0" 
RUN mim install "mmdet==3.0.0"
RUN mim install git+https://github.com/onuralpszr/mmyolo.git

# Install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


RUN mkdir -p yolo
WORKDIR /yolo

