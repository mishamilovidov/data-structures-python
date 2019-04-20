#!/usr/bin/env python3
import sys
import csv
import math

class ScheduleSolution(object):
  '''
  An object to represent a complete schedule solution
  '''
  
  def __init__(self, slots, classes_csv):
    '''Creates a schedule solution based on rooms available and classes to assign'''
    self.available_slots = slots
    self.class_list = self._generate_class_list(classes_csv)
    self.data = {}
    
  def _generate_class_list(self, classes_csv):
    '''Generates a list of individual classes from csv of classes'''
    with open(classes_csv) as input_file:
      class_list = []
      class_attributes = []
      csv_reader = csv.reader(input_file, delimiter=',')
      
      for idx, row in enumerate(csv_reader):
        if idx == 0:
          for item in row:
            class_attributes.append(item.strip().lower().replace(' ','_'))
        else:
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
    single_class['slots'] = math.ceil((float(single_class['hours']) + 0.25) / 0.5)
    del single_class['sections']
      
    return single_class
    
  def getFitness(self):
    '''Calculates the fitness of the schedule solution'''
    
    
  def crossover(self, other_solution):
    '''Crosses with another scheudled solution and returns a new schedule solution'''
    
    
  def mutate(self):
    '''Mutates the schedule solution in some way'''
    

###################################################
###   Utilities