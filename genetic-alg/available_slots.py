#!/usr/bin/env python3
import sys
import csv

DAY_HOUR_START = 8
DAY_HOUR_END = 17
SLOTS_PER_HOUR = 2
SLOTS_PER_DAY = (DAY_HOUR_END - DAY_HOUR_START) * SLOTS_PER_HOUR + 1
DAY_LIST = ['M', 'T', 'W', 'Th', 'F']

class AvailableSlots(object):
  '''
  An object that represents the available slots on the building schedule
  '''
  
  def __init__(self, ROOMS_CSV):
    '''Creates a set for the available slots on a schedule'''
    with open(ROOMS_CSV) as input_file:
      self.data = set()
      csv_reader = csv.reader(input_file, delimiter=',')
      line = 0
      
      for row in csv_reader:
        if line != 0:
          room = row[0]
          capacity = row[1]
          type = row[2]
          
          for slot in range(1, SLOTS_PER_DAY):
            for day in DAY_LIST:
              self.data.add('{}-{}-{}-{}-{}'.format(room, day, slot, capacity, type))
      
        line += 1
    
  def getFreeSlots(self, length, num_days):
    '''Returns an available slot based on the slot length and num of days'''
    return None
    
    