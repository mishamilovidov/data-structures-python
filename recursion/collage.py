#!/usr/bin/env python3
import argparse
import os
import math
from PIL import Image               # pip3 install pillow
from foldersearch import find_images


THUMBNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200
THUMBNAIL_SIZE = THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT
IMAGE_WIDTH = THUMBNAIL_WIDTH * THUMBNAILS_PER_ROW


########################
###  Main program

def main(args):
  '''
  Creates a collage by recursively finding images in a directory path.
  '''
  # find the images
  imgpaths = []
  for filepath in find_images(os.path.abspath(args.searchpath)):
    imgpaths.append(filepath)
  if len(imgpaths) == 0:
    print('No images found')
    return
    
  # determine image height
  IMAGE_ROWS = math.ceil(len(imgpaths)/THUMBNAILS_PER_ROW)
  IMAGE_HEIGHT = IMAGE_ROWS * THUMBNAIL_HEIGHT

  # create a new, RGB image
  image_dims = (IMAGE_WIDTH, IMAGE_HEIGHT)
  image = Image.new('RGB', image_dims, color = (0, 0, 0)) 

  # place the thumbnails
  for imgnum, imgpath in enumerate(imgpaths):
  
    # open the image and convert to RGB
    img = Image.open(imgpath).convert('RGB')
    
    # resize to a thumnail
    img.thumbnail(THUMBNAIL_SIZE)
    
    # paste in next position
    x_pos = (imgnum%THUMBNAILS_PER_ROW) * THUMBNAIL_WIDTH
    y_pos = math.floor(imgnum/THUMBNAILS_PER_ROW) * THUMBNAIL_HEIGHT
    image.paste(img, (x_pos, y_pos))

  # save the image
  image.save(args.collage)


########################
###  Bootstrap

parser = argparse.ArgumentParser(description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
