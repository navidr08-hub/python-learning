# Chapter 21 - Graphs and Manipulating Images
# (Practice Program) - Tile Maker
# calling make_tile('zophie_the_cat.jpg', 6, 10) should return a 120×500 image with 60 tiles total

import sys
import argparse
import random
from PIL import Image, ImageOps


def make_tile(filepath, tiles_length, tiles_height):
    try:
        im = Image.open(filepath)
        width, height = im.size
        resized_im = ImageOps.fit(im, (width//10, height//10))
        r_width, r_height = resized_im.size

        t_width, t_height = (r_width * tiles_length, r_height * tiles_height)
        tile_im = Image.new('RGBA', (t_width, t_height), 'white')

        for row in range(tiles_height):
            for col in range(tiles_length):
                rot = random.choice([90, 180, 270])
                tile_im.paste(resized_im.rotate(rot), (col * r_width, row * r_height))

        tile_im.show()

    except FileNotFoundError:
        print("File was not found, invalid filepath to image.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Create a multiplication table provided a number."
    )
    
    # Add some positional arguments
    parser.add_argument("filepath", type=str, help="Path to image file")
    parser.add_argument("columns", type=int, help="Number of columns")
    parser.add_argument("rows", type=int, help="Number of rows")

    args = parser.parse_args()
    make_tile(args.filepath, args.columns, args.rows)


if __name__ == "__main__":
    main()