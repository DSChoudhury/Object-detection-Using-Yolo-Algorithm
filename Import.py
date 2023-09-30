!git clone https://github.com/ultralytics/yolov5  # clone ultralytics model from Ultralytics github official site
%cd yolov5 #open yolov5
%pip install -qr requirements.txt comet_ml  # install requirements.txt to install ll the necessary libraries

import torch
import utils
display = utils.notebook_init()  # checks status