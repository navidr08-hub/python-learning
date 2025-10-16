# Chapter 22 - Recognizing Text in Images
# (Practice Program) - Browser Text Scraper
# Windows 10 ONLY

"""
A web page showing a book chapter on the lefthand side 
and the text 'Annoying sidebar ads here!' On the righthand side.
The PyAutoGUI library covered in Chapter 23 can take screenshots
and save them to an image, while the Pillow library covered in Chapter 21 can crop images. 
PyAutoGUI also has a MouseInfo application for finding XY coordinates on the screen.
Write a program named ocrscreen.py that takes a screenshot, crops the image to just 
the text portion in the screenshot, then passes it on to PyTesseract for OCR. 
The program should append the recognized text to the end of a text file named output.txt. 
Here is a template for the ocrscreen.py program
"""

import os
import pyautogui
import cv2
import numpy as np
import time
import pytesseract as tess
from PIL import Image


TEST_IMG_FILE = "C:\\Users\\navid\\Documents\\programs\\static\\ocr_example.png"
SCNSHOT_FILE = "C:\\Users\\navid\\Documents\\programs\\output\\screenshot.png"
OUTPUT_DIR = "C:\\Users\\navid\\Documents\\programs\\output"

LEFT = 400
TOP = 200
RIGHT = 1000
BOTTOM = 800


def crop_img(im):
    """Take image object from pillow, convert to cv2 image, crop it, return it"""
    cv2_im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    r = cv2.selectROI("Select Region to Crop", cv2_im, fromCenter=False, showCrosshair=True)
    x, y, w, h = r
    return cv2_im[int(y):int(y+h), int(x):int(x+w)]


def save_screenshot():
    """Take screenshot, crop it, save it"""
    print("Taking screenshot in 3s:")
    print("3...")
    time.sleep(2)
    print("2...")
    time.sleep(2)
    print("1...")
    time.sleep(2)
    
    im = pyautogui.screenshot()
    cv2_im = crop_img(im)
    cv2.imwrite(SCNSHOT_FILE, cv2_im)


def scan_image(im_fp: str):
    im = Image.open(im_fp)
    text = tess.image_to_string(im)
    return text


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    save_screenshot()
    time.sleep(1)
    print(scan_image(SCNSHOT_FILE))
    
if __name__ == "__main__":
    main()
