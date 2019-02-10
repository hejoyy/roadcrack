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
               location = path+filename
               if 'Base' not in location:
                    image_list.append(location)
    return image_list


def get_images_location(crack_type):
     """dataset 폴더 안의 모든 이미지 중에 crack_type에 해당하는 images location 리턴

     '''./datasets/external'''에 imgae dataset 위치

     """
     all_images_loc = get_all_images_location('/Volumes/JOBS/01. 2016년 조사자료(3단계)')
     query_data = pd.read_excel('./query_data/' + crack_type + '.xlsx')
     image_names = query_data.RDSRFC_IMG_FILE_NM_1.values
     selected_images_location = []
     for image_name in image_names:
         for location in all_images_loc:
             if image_name in location:
                 selected_images_location.append(location)
     return selected_images_location


crack_type = 'AC_HI_QR'
# AC_HI_QR_images_location = get_images_location('AC_HI_QR')
# print(AC_HI_QR_images_location)


query_data = pd.read_excel('/Users/hejoyy/Desktop/project/RoadCrack/query_data/' + crack_type + '.xlsx')
image_names = query_data.RDSRFC_IMG_FILE_NM_1.values


all_images_loc = get_all_images_location('/Volumes/JOBS/01. 2016년 조사자료(3단계)')

# print(all_images_loc)
# image_names
print(all_images_loc[0])
print('개화동로' in all_images_loc[0])
