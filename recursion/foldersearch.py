#!/usr/bin/env python3
import os
import fnmatch


IMAGE_GLOBS = {
  '*.png',
  '*.jpg',
}

def is_image(filename):
  matches = 0

  for glob in IMAGE_GLOBS:
    if fnmatch.fnmatch(filename, glob):
      matches += 1
      
  if matches > 0:
    return True
  else:
    return False

def find_images(dirpath):
  for filename in os.listdir(dirpath):
    fullpath = os.path.join(dirpath, filename)
    
    if os.path.isdir(fullpath):
      yield from find_images(fullpath)
      
    elif is_image(fullpath):
      yield fullpath