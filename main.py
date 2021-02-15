from util import *
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
    def __init__(self, _img):
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
    
    #def form_wafer(self, frame_list):

i = 1
#Load input data
data = load_input('Level_1_data/input.json')
im = load_image(f'Level_1_data/wafer_image_1.png')
dimension_of_frame = im.shape
print(dimension_of_frame)

#Dimension of Wafer
dimension_of_wafer = (data["die"]["width"]*data["die"]["columns"], data["die"]["height"]*data["die"]["rows"])
print(dimension_of_wafer)
Wafer_frame_dimn = (dimension_of_wafer[0]/dimension_of_frame[0], dimension_of_wafer[1]/dimension_of_frame[1])

#Number of images in the file
number_of_image = get_number_images('Level_1_data')

#Main datasets
frame_list = []
die_list = []

#Standard dev
std_dev = []

#Mean 
mean_value = []

#Anamoly
anamoly = []

#wafer
wafer = load_image(f'Level_1_data/wafer_image_1.png')
print(wafer)
wafer = np.reshape(wafer, (1, dimension_of_frame[0], dimension_of_frame[1]))
print("\n\n\n",wafer)
for i in range(2, number_of_image+1):
    img = load_image(f'Level_1_data/wafer_image_{i}.png')
    img = np.reshape(img, (1, dimension_of_frame[0], dimension_of_frame[1]))
    #inst = Frame(img)
    #frame_list.append(inst)
    wafer = np.append(wafer, img, axis=0)

wafer_size = wafer.shape
frame_size = (wafer_size[1], wafer_size[2])

print(wafer_size, frame_size)
#print(wafer)
#Calculate upper and lower value using standard deviation
upper = np.zeros(frame_size, dtype = int)
lower =  np.zeros(frame_size, dtype = int)
print(wafer[:, 0, 0])
for i in range(dimension_of_frame[0]):
    for j in range(dimension_of_frame[1]):
        lower[i, j], upper[i, j] = get_average(wafer[:, i, j])

for i in range(wafer_size[0]):
    for j in range(frame_size[0]):
        for k in range(frame_size[1]):
            #print(lower[j][k], lower[j][k], wafer[i, j, k])
            if(check_anomalies(wafer[i, j, k], lower[j][k], upper[j][k])):
                
                anamoly.append((i, j, k))
print(lower)
print(upper)       
print(anamoly)

# for i in frame_list:
#     inst = Die(i.img)
#     die_list.append(inst)

# for i in frame_list:
#     wafle = np.concatenate
