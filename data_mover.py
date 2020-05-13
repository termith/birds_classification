import os
import shutil
import random
import pathlib
import argparse


def move_images(dest, data_path, validation_size):
    dst = pathlib.Path(dest)
    train_folder = dst / 'train'
    os.makedirs(train_folder, exist_ok=True)
    valid_folder = dst / 'validation'
    os.makedirs(valid_folder, exist_ok=True)

    src = pathlib.Path(data_path)
    for folder in os.listdir(src):
        if str(folder).startswith('.'):
            continue
        # Caltech Birds dataset folder names look like 001.Black_footed_Albatross
        class_name = folder.split('.')[-1].split('_')[-1]
        class_valid_folder = valid_folder / class_name
        class_train_folder = train_folder / class_name
        os.makedirs(class_train_folder, exist_ok=True)
        os.makedirs(class_valid_folder, exist_ok=True)

        for filename in os.listdir(src/folder):
            if random.randint(0, 100) < int(validation_size):
                shutil.copy(src/folder/filename, class_valid_folder/filename)
            else:
                shutil.copy(src/folder/filename, class_train_folder/filename)

    shutil.rmtree(src)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', help='Path to the data')
    parser.add_argument('--dest', help='Destination of new dataset')
    parser.add_argument('--validation_size', help='Validation set percent')
    args = parser.parse_args()

    move_images(args.dest, args.data_path, args.validation_size)

