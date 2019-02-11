#-*-coding: utf-8

import os
import pandas as pd
import numpy as np

def get_all_images_location(dataset_dir):
    image_list = []
    for (path, dir, files) in os.walk(dataset_dir):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg':
               location = path+'/'+filename
               if 'Base' not in location:
                    image_list.append(location)
    return image_list


img_loc = get_all_images_location('/Volumes/JOBS/01. 2016년 조사자료(3단계)')
img_loc

import shutil
dir = '/Volumes/JOBS/datasets/'
for loc in img_loc:
    src = loc
    shutil.move(src, dir)
