import pandas as pd
import numpy as np
from PIL import Image

def get_image_names(crack_type):
    """dataset 폴더 안의 모든 이미지 중에 crack_type에 해당하는 image vector 리턴

    이거는 해당 crack_type 엑셀에서 이미지이름 긁어오는거
    """

    query_data = pd.read_excel('./query_data/' + crack_type + '.xlsx')
    image_names = query_data.RDSRFC_IMG_FILE_NM_1.values

    return image_names

def get_image_vector(crack_type):
    """dataset 폴더 안의 모든 이미지 중에 crack_type에 해당하는 image vector 리턴
       datasets_dir은 외장하드 root directory에 datasets 폴더에 이미지
    """
    datasets_dir = '/Volumes/JOBS/datasets/'
    image_names = get_image_names(crack_type)
    image_list = []
    for image_name in image_names:
        img = Image.open(datasets_dir + image_names)
        image_list.append(img)

    return np.asarray(image_list)

# example
data_ACHIQR = get_image_vector('AC_HI_QR')
