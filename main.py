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
    
    def isIn(self, x, y):
        if(self.xmin <= x and self.xmax >= x and self.ymin <= y and self.ymax >= y):
            return True
        return False

class ExclusionZone:
    def __init__(self, _xmin, _xmax, _ymin, _ymax):
        self.xmin = _xmin
        self.xmax = _xmax
        self.ymin = _ymin
        self.ymax = _ymax
    
    def isNotIn(self, x, y):
        if(self.xmin <= x and self.xmax >= x and self.ymin <= y and self.ymax >= y):
            return False
        return True

class Wafer:
    def __init__(self, _path, size):
        wafer = []
        for i in range(size[0]):
            for j in range(size[1]):
                coord = 0
                if i%2 == 0:
                    coord = i*size[1] + j + 1
                else:
                    coord = i*size[1] + size[0] - j 
                image_path = f'Level_1_data/wafer_image_{coord}.png'
                img = load_image(image_path)
                wafer.append(img)
        self.matrix = np.array(wafer)
        self.matrix.share = size
        self.size = size

#Load initial inputs
data = load_input('Level_1_data/input.json')


careAreaList = []
for area in range(data["care_areas"]):
    corn1 = area["top_left"]
    corn2 = area["bottom_right"]
    careAreaList.append(CareArea(corn1["x"], corn2["x"], corn1["y"], corn2["y"]))

exclusionZonesList = []
for area in range(data["exclusion_zones"]):
    corn1 = area["top_left"]
    corn2 = area["bottom_right"]
    exclusionZonesList.append(CareArea(corn1["x"], corn2["x"], corn1["y"], corn2["y"]))

dieList = []

class Die:
    def __init__(self, img, id):
        self.id = id
        self.img = img
    
    
class Anamoly:
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col

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
Wafer_frame_dimn = (dimension_of_wafer[0]//dimension_of_frame[0], dimension_of_wafer[1]//dimension_of_frame[1])

#Number of images in the file
number_of_image = get_number_images('Level_1_data')

#Anamoly
anamoly = set()

#wafer
wafer = []
print(wafer)
print("\n\n\n",wafer)

n = Wafer_frame_dimn
for i in range(n[0]):
    for j in range(n[1]):
        coord = 0
        if i%2 == 0:
            coord = i*n[1] + j + 1
        else:
            coord = i*n[1] + n[0] - j 
        path_ = f'Level_1_data/wafer_image_{coord}.png'
        img = load_image(f'Level_1_data/wafer_image_{i}.png')
        wafer.append(img)
    
wafer = np.array(wafer)
wafer.shape = (n[0], n[1])




for i in range(2, number_of_image+1):
    img = load_image(f'Level_1_data/wafer_image_{i}.png')
    wafer = np.append(wafer, img, axis=0)

wafer_size = wafer.shape
frame_size = (wafer_size[1], wafer_size[2])
street_size = data["street_width"]

print(wafer_size, frame_size)


#Comparing first and last frame with 2 frames consecutively
last_idx = wafer_size[0] - 1
for j in range(0, frame_size[0]):
        for k in range(0, frame_size[1]):
            if(abs(wafer[0, j, k] - wafer[1, j, k]) > 4 and abs(wafer[0, j, k] - wafer[2, j, k]) > 4):
                anamoly.add((1, j, k ))
            if(abs(wafer[last_idx, j, k] - wafer[last_idx-1, j, k]) > 4 and abs(wafer[last_idx, j, k] - wafer[last_idx-2, j, k]) > 4):
                anamoly.add((last_idx + 1, j, k))

#Comparing before and previous frame
for i in range(1, wafer_size[0]-1):
    for j in range(0, frame_size[0]):
        for k in range(0, frame_size[1]):
            if(abs(wafer[i, j, k] - wafer[i-1, j, k]) > 4 and abs(wafer[i, j, k] - wafer[i+1, j, k]) > 4):
                anamoly.add((i+1, j, k))


print(anamoly)



# # for i in frame_list:
# #     inst = Die(i.img)
# #     die_list.append(inst)

# # for i in frame_list:
# #     wafle = np.concatenate
