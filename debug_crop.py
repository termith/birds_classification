from pathlib import Path

from fastai.vision import ImageDataBunch, get_transforms, imagenet_stats

from data_mover import move_images
from img_cropper import crop_images

ROOT_PATH = '/Users/ddemidov/Desktop/CUB_200_2011/CUB_200_2011/'
BB_FILE = ROOT_PATH + 'bounding_boxes.txt'
IMAGES_PATH = ROOT_PATH + 'images'
IDS_FILE = ROOT_PATH + 'images.txt'

if __name__ == '__main__':
    # crop_images(IDS_FILE, IMAGES_PATH, BB_FILE)
    # move_images('./images', IMAGES_PATH, 20)

    data = ImageDataBunch.from_folder(Path('./images'), ds_tfms=get_transforms(), valid='validation', size=299, bs=32).normalize(imagenet_stats)

    data.show_batch(2, 3)
