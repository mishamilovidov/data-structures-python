#!/usr/bin/env python3
import sys
import csv
import math
import random

BREAK_TIME = 0.25
SLOT_DURATION = 0.5

class Courses(object):
  '''
  An object that represents the courses that need to be scheduled
  '''
  
  def __init__(self, classes_csv):
    '''Creates a list of courses that need to be scheduled'''
    self.data = self._generate_data(classes_csv)

  
  def _generate_data(self, classes_csv):
    '''Generates a list of individual classes from csv of classes'''
    class_items = []
    class_list = []
    class_attributes = []
    
    with open(classes_csv) as input_file:
      csv_reader = csv.reader(input_file, delimiter=',')
      for row in csv_reader:
        class_items.append(row)
      
    for item in class_items[0]:
      class_attributes.append(item.strip().lower().replace(' ','_'))
    
    class_items.remove(class_items[0])
    random.shuffle(class_items)
  
    for row in class_items:
      num_sections = int(row[6])
      for section in range(1, num_sections + 1):
        single_class = self._generate_single_class(class_attributes, row, section)
        class_list.append(single_class)
        
    return class_list
    
    
  def _generate_single_class(self, class_attributes, class_data, section):
    '''Generates a single class dictionary'''
    single_class = {}
    for idx, item in enumerate(class_data):
      single_class[class_attributes[idx]] = item
  
    single_class['section'] = section
    single_class['slots'] = math.ceil((float(single_class['hours']) + BREAK_TIME) / SLOT_DURATION)
      
    return single_class