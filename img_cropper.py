"""
From Dataset documentation:
=========================
BOUNDING BOXES:
=========================

Each image contains a single bounding box label.  Bounding box labels are contained in the file bounding_boxes.txt, with each line corresponding to one image:

<image_id> <x> <y> <width> <height>

where <image_id> corresponds to the ID in images.txt, and <x>, <y>, <width>, and <height> are all measured in pixels
"""
import pathlib
import argparse

from PIL import Image


def crop_images(ids_file, data_path, bb_file):
    max_width = 0
    max_height = 0
    with open(bb_file, 'r') as f:
        # boundaries for image_id = boundaries[image_id - 1]
        boundaries = [tuple(map(float, line.split())) for line in f.readlines()]
    with open(ids_file) as idf:
        for line in idf.readlines():
            id_, image_file = line.split()
            image_path = pathlib.Path(data_path)/image_file
            _, x, y, w, h = boundaries[int(id_)-1]
            if w > max_width:
                max_width = w
            if h > max_height:
                max_height = h
            Image.open(image_path).crop((x, y, x+w, y+h)).save(image_path)
    print(f'Max width: {max_width}, max height: {max_height}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ids_file', help='Path to file with images id mapping')
    parser.add_argument('--data_path', help='Path to images')
    parser.add_argument('--bb_file', help='Path to file with bounding boxes attributes')

    args = parser.parse_args()

    crop_images(args.ids_file, args.data_path, args.bb_file)

