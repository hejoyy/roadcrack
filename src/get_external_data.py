import os

def get_image_location(dataset_dir, crack_type=False):
    """dataset directory 안의 image의 상대경로 리턴

    dataset_dir : dataset folder directory name
    crack_type : crack type of images
    """
    image_list = []
    for (path, dir, files) in os.walk(dataset_dir):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg':
               location = path+filename
               if 'Base' not in location:
                    image_list.append(location)
    return image_list

images_loc = get_image_location("./datasets/external")
len(images_loc)
images_loc
