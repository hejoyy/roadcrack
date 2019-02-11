#-*-coding: utf-8

import os
import pandas as pd
import numpy as np


# 맥에다 외장하드 꼽고 돌리는겨
# 이미지 한폴더에 모으는 작업 개오래걸림
# 40분 돌렸는데 아직 다안뎀 개뜨거워서 하다 멈춤

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
