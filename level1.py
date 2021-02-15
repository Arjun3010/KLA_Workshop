from util import *
import pandas as pd
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
# class Anamoly:
#     def __init__(self, id, row, col):
#         self.id = id
#         self.row = row
#         self.col = col

#     def calculate_anamoly(height, row, col, die_size, frame_size, street_size):
#         r = height*frame_size[0] + 
class Wafer:
    def __init__(self):
        self.data = None
    
    #def form_wafer(self, frame_list):

i = 1
#Load input data
data = load_input('Level_1_data/input.json')
dimension_of_frame = load_image(f'Level_1_data/wafer_image_1.png').shape

print(dimension_of_frame)

#Dimension of Wafer
die_size = (data["die"]["width"], data["die"]["height"])
dimension_of_wafer = (data["die"]["width"]*data["die"]["columns"] + data["street_width"] * (data["die"]["columns"] - 1)
                        , data["die"]["height"]*data["die"]["rows"] + data["street_width"] * (data["die"]["rows"] - 1))
print(dimension_of_wafer)
Wafer_frame_dimn = (dimension_of_wafer[0]/dimension_of_frame[0], dimension_of_wafer[1]/dimension_of_frame[1])

#Number of images in the file
number_of_image = get_number_images('Level_1_data')

#Main dataanamolys
frame_list = []

#Standard dev
std_dev = []

#Mean 
mean_value = []

#Anamoly
anamoly = set()

#wafer
wafer = load_image(f'Level_1_data/wafer_image_1.png')
print(wafer)
wafer = np.reshape(wafer, (1, dimension_of_frame[0], dimension_of_frame[1]))
print("\n\n\n",wafer)
for i in range(2, number_of_image+1):
    img = load_image(f'Level_1_data/wafer_image_{i}.png')
    img = np.reshape(img, (1, dimension_of_frame[0], dimension_of_frame[1]))
    wafer = np.append(wafer, img, axis=0)

wafer_size = wafer.shape
frame_size = (wafer_size[1], wafer_size[2])
street_size = data["street_width"]
die_size = (data["die"]["height"], data["die"]["width"])

print(wafer_size, frame_size)

for j in range(0, die_size[0]):
    for k in 


#Comparing first and last frame with 2 frames consecutively
last_idx = wafer_size[0] - 1
for j in range(0, frame_size[0]):
    for k in range(0, frame_size[1]):
        if(abs(wafer[0, j, k] - wafer[1, j, k]) > 4 and abs(wafer[0, j, k] - wafer[2, j, k]) > 4):
            anamoly.add((1, j, k ))
        if(abs(wafer[last_idx, j, k] - wafer[last_idx-1, j, k]) > 4 and abs(wafer[last_idx, j, k] - wafer[last_idx-2, j, k]) > 4):
            anamoly.add((last_idx + 1,frame_size[0] - 1 - j, k))

#Comparing before and previous frame
for i in range(1, wafer_size[0]-1):
    for j in range(0, frame_size[0]):
        for k in range(0, frame_size[1]):
            if(abs(wafer[i, j, k] - wafer[i-1, j, k]) > 4 and abs(wafer[i, j, k] - wafer[i+1, j, k]) > 4):
                anamoly.add((i+1,frame_size[0] - 1 - j, k))

l = list(anamoly)
df = pd.DataFrame.from_records(l)
df.to_csv('output.csv', header=False, index=False)
print(df)

# # for i in frame_list:
# #     inst = Die(i.img)
# #     die_list.append(inst)

# # for i in frame_list:
# #     wafle = np.concatenate
