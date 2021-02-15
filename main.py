from utils import *
import json
import pandas
import os
import cv2
import numpy as np
import math


class CareArea:
    def __init__(self, _xmin, _xmax, _ymin, _ymax):
        self.xmin = _xmin
        self.xmax = _xmax
        self.ymin = _ymin
        self.ymax = _ymax

class Frame:
    number_of_frames = 0
    def __init__(self, _img)
        Frame.number += 1
        self.id = Frame.number_of_frames + 1
        self.image = _img
        self.size = self.image.shape

class Die:
    number_of_dies = 0
    def __init__(self, _img):
        Die.number_of_dies += 1
        self.id = Die.number_of_dies
        self.img = _img
        self.size = img.shape()

class Wafer:
    def __init__(self):
        self.data = None
    
    def form_wafer(self, frame_list):
        
i = 1
data = load_input('Level_1_data/input.json')
im = load_image(f'Level_1_data/wafer_image_{0}.png')
dimension_of_frame = im.shape

#Dimension of Wafer
dimension_of_wafer = (data["die"]["width"]*data["die"]["column"], data["die"]["height"]*data["die"]["column"])
Wafer_frame_dimn = (dimension_of_wafer[0]/dimension_of_frame[0], dimension_of_wafer[1]/dimension_of_frame[1])

#Number of images in the file
number_of_image = get_number_images()

#Main datasets
frame_list = []
die_list = []

#Standard dev
std_dev = []

#Mean 
mean_value = []

#wafle

img = load_image(f'Level_1_data/wafer_image_{0}.png')

for i in range(2, number_of_images):
    img = load_image(f'Level_1_data/wafer_image_{0}.png')
    inst = Frame(img)
    frame_list.append(inst)
    wafer.append()

for i in frame_list:
    inst = Die(i.img)
    die_list.append(inst)

wafle = []
for i in frame_list:
    wafle = np.concatenate
def check_anomalies(self, curr, pixels):
    anomalies = []
    std_dev = np.std(pixels)
    mean_value = np.mean(pixels)
    anamoly_cutoff = std_dev * 3
    lower = mean_value - anamoly_cutoff
    upper = mean_value + anamoly_cutoff
    return (curr > upper or curr < lower)
