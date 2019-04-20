#!/usr/bin/env python3
import sys

DAY_HOUR_START = 8
DAY_HOUR_END = 17
SLOTS_PER_HOUR = 2
SLOTS_PER_DAY = (DAY_HOUR_END - DAY_HOUR_START) * SLOTS_PER_HOUR + 1
DAY_LIST = ['M', 'T', 'W', 'Th', 'F']

class Slots(object):
  '''
  An object that represents the available slots for the building schedule
  '''
  
  def __init__(self, rooms):
    '''Creates a set for the available slots on a schedule'''
    self.data = self._generate_data(rooms)
    
    
  def get_free_slots(self, length, num_days):
    '''Returns an available slot based on the slot length and num of days'''
    return None
    
    
  def _generate_data(self, rooms):
    '''Generates set of available slots from list of rooms'''
    slots_set = set()
    
    for room in rooms:
      for slot in range(1, SLOTS_PER_DAY):
        for day in DAY_LIST:
          slots_set.add('{}-{}-{}-{}-{}'.format(room['room'], day, slot, room['capacity'], room['type']))
          
    return slots_set