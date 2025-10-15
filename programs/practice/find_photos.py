# Chapter 21 - Graphs and Manipulating Images
# (Practice Program) - Identifying Photo Folders on the Hard Drive

import os
import argparse
from PIL import Image, UnidentifiedImageError


def find_photos(base_dir: str):
    found = False

    # Import modules and write comments to describe this program.
    if not os.path.isdir(base_dir):
        raise Exception("Invalid directory path")
    
    # if not os.path.isabs(base_dir):
    #     base_dir = os.path.abspath(base_dir)
    
    for folder_name, subfolders, filenames in os.walk(base_dir):
        num_photo_files = 0
        num_non_photo_files = 0
        for filename in filenames:
            # Check if the file extension isn't .png or .jpg.
            if not (filename.endswith('.png') or filename.endswith('.jpg')):
                num_non_photo_files += 1
                continue  # Skip to the next filename.

            # Open image file using Pillow.
            filepath = os.path.join(base_dir, folder_name, filename)
            try:
                im = Image.open(filepath)
            except UnidentifiedImageError:
                continue
            
            width, height = im.size

            # Check if the width & height are larger than 500.
            if width > 500 and height > 500:
                # Image is large enough to be considered a photo.
                num_photo_files += 1
            else:
                # Image is too small to be a photo.
                num_non_photo_files += 1

        # If more than half of files were photos,
        # print the absolute path of the folder.
        if num_photo_files > num_non_photo_files:
            found = True
            print("Photo folder:")
            print(os.path.abspath(os.path.join(base_dir, folder_name)))

    if not found:
        print("Photo folder was not found in this drive.")
            

def main():
    parser = argparse.ArgumentParser(
        description="Find if any photo folders are present in given folder path."
    )
    
    # Add some positional arguments
    parser.add_argument("directory", type=str, help="Path to directory/drive file")

    args = parser.parse_args()
    find_photos(args.directory)


if __name__ == "__main__":
    main()