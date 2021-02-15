import json
import os
import cv2
import numpy
import math

def load_input(_path : str):
    with open(_path) as json_file:
        data = json.load(json_file)
    return data

def load_image(_path : str):
    img = cv2.imread(_path, 0)
    return img

class CareArea:
    def __init__(self, _xmin, _xmax, _ymin, _ymax):
        self.xmin = _xmin
        self.xmax = _xmax
        self.ymin = _ymin
        self.ymax = _ymax


class Frame:
    number_of_frames = 0
    def __init__(self, _filename, _die_id):
        self.die_id = _die_id
        Frame.number += 1
        self.index = Frame.number_of_frames + 1
        self.image = load_image(_filename)
        self.size = self.image.shape

class Die:
    number_of_dies = 0
    def __init__(self, _img, _id):
        Die.number_of_dies += 1
        self.id = Die.number_of_dies
        self.img = _img
        self.size = img.shape()

i = 1
im = load_image(f'Level_1_data/wafer_image_{i}.png')
dimension_of_frame = im.shape
number_of_images = len([name for name in os.listdir('./Level_1_data') if os.path.isfile(name)])
while(True):
    try:
        im = load_image(f'Level_1_data/wafer_image_{i}.png')
    

data = load_input('Level_1_data/input.json')
img = load_image('Level_1_data/wafer_image_1.png')