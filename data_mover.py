import os
import shutil
import random
import pathlib
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', help='Path to the data')
    parser.add_argument('--dest', help='Destination of new dataset')
    parser.add_argument('--validation_size', help='Validation set percent')
    args = parser.parse_args()

    dst = pathlib.Path(args.dest)
    train_folder = dst / 'train'
    os.makedirs(train_folder, exist_ok=True)
    valid_folder = dst / 'validation'
    os.makedirs(valid_folder, exist_ok=True)

    src = pathlib.Path(args.data_path)
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
            if random.randint(0, 100) < int(args.validation_size):
                shutil.move(src/folder/filename, class_valid_folder/filename)
            else:
                shutil.move(src/folder/filename, class_train_folder/filename)

    shutil.rmtree(src)