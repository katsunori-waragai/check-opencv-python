FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3

RUN apt-get update
RUN apt install sudo
# only for development
RUN apt update && apt install -y eog nano
RUN apt install -y meshlab


RUN cd /root ; mkdir check-opencv-python
RUN cd /root/check-opencv-python
WORKDIR /root/check-opencv-python
COPY *.py ./
RUN python3 -m pip install gdown
COPY pyproject.toml ./

WORKDIR /root/check-opencv-python

RUN python3 -m pip install .[dev]
