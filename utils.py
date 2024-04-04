from PIL import Image
import os

def clear_folder(folder_path):
    for file_name in os.listdir(folder_path):
        FilePath = os.path.join(folder_path + file_name)
        os.remove(FilePath)


def scaling_images_in_folder(folder_path):
    for index, file_name in enumerate(os.listdir(folder_path), start = 1):
        with Image.open(folder_path + file_name) as image:
            image.thumbnail((512, 512))
            image.save('ModifiedImages/scaled-image-' + str(index) + '.png')

def create_files_list(folder_path):
    files_list = []
    for file_name in os.listdir(folder_path):
        files_list.append(file_name)
    return files_list