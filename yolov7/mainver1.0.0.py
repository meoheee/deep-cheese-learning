import os
import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

#initial setting
device = select_device('')
half = device.type != 'cpu'  # half precision only supported on CUDA
model = attempt_load('best_494.pt', map_location=device)
stride = int(model.stride.max())  # model stride
imgsz = check_img_size(640, s=stride)

#class load and color select
names = model.module.names if hasattr(model, 'module') else model.names
colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]
colors = [[255,0,0], [0,0,0]]

if half:
    model.half()  # to FP16 becuase cuda should not FP32

if device.type != 'cpu':
    model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
old_img_w = old_img_h = imgsz
old_img_b = 1

files = os.listdir('photo')
for file in files:

    #Image Load
    source = 'photo/' + file
    dataset = LoadImages(source, img_size=imgsz, stride=stride)

    t0 = time.time()
    for path, img, im0s, vid_cap in dataset:

        #Img -> Tensor
        img = torch.from_numpy(img).to(device)

        #Tensor Quantanization half
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        with torch.no_grad():   # Calculating gradients would cause a GPU memory leak
            pred = model(img, augment= True)[0]
        t2 = time_synchronized()

        # Apply NMS
        conf = 0.25
        iou = 0.45
        pred = non_max_suppression(pred, conf, iou, agnostic = False)
        t3 = time_synchronized()

        # result show
        for i, det in enumerate(pred):  # detections per image

            # file write
            for *xyxy, conf, cls in reversed(det):
                if int(cls) == 1:
                    label = f'{names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, im0s, label=label, color=colors[int(cls)], line_thickness=1)
            cv2.imwrite('result/' + file, im0s)


            # Print time (inference + NMS)
            print(f'{file} Done. ({(1E3 * (t2 - t1)):.1f}ms) Inference, ({(1E3 * (t3 - t2)):.1f}ms) NMS')