import json
import os 
import cv2
import numpy as np

def load_input(_path : str):
    with open(_path) as json_file:
        data = json.load(json_file)
    return data

def get_number_images(_path : str):
    cwd = os.getcwd() + '\\' + _path
    entries = os.listdir(cwd)
    return len(entries) - 1

def load_image(_path : str):
    img = cv2.imread(_path, 0)
    return img
