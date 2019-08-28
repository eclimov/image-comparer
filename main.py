from os import listdir, remove, path, makedirs
from os.path import isfile, join

def get_image_list(folder_path):
    only_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    return only_files

images = get_image_list('./images')
for image_name_i in images:
    for image_name_j in images:
        if image_name_i != image_name_j:
            print(f'{image_name_i} - {image_name_j}')
