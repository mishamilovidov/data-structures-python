#!/usr/bin/env python3
import sys
import random

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
    self.slots_used = 0
    
  
  def __iter__(self):
    '''Iterates through the linked list, implemented as a generator.'''
    for key, value in self.data.items():
        yield (key, value)
    
    
  def get_free_slots(self, days, slot_count, min_capacity):
    '''Returns an available slot based on the slot length and num of days'''
    available_slots = []
    
    if len(days) > 1:
      day_one_slots = self._find_available_slot_block(days[0], slot_count, min_capacity)
      
      if len(day_one_slots) > 0:
        day_two_slots = self._find_available_slot_block(days[1], slot_count, min_capacity, day_one_slots[0])
      else:
        day_two_slots = []
        
      return day_one_slots + day_two_slots
    else:
      day = days[0]
      return self._find_available_slot_block(day, slot_count, min_capacity)    
    
    
  def _find_available_slot_block(self, day='M', slot_count=None, min_capacity=None, match_slot=None):
    '''Finds available block of slots for specific day of the week'''
    slot_block = []
    
    for slot_key, slot in self.data.items():
      slot_code = slot_key.split('-')
      room = slot_code[0]
      day_code = slot_code[1]
      slot_num = int(slot_code[2])
      capacity = int(slot_code[3])
      type = slot_code[4]
      base_slot_check = slot.available and capacity >= min_capacity and ((slot_num  + slot_count) <= SLOTS_PER_DAY) and day == day_code
      matches = 0
      
      for i in range(slot_num, (slot_num + slot_count)):
        key = '{}-{}-{}-{}-{}'.format(room, day_code, i, capacity, type)
        try:
          if self.data[key].available:
            matches = matches + 1
        except:
          matches = matches
        
      availablitiy_slot_check = matches == ((slot_count - slot_num) + 1)
      
      if match_slot:
        match_slot_code = match_slot.data.split('-')
        
        if base_slot_check and availablitiy_slot_check and slot_num == int(match_slot_code[2]) and room == match_slot_code[0]:
          for i in range(slot_num, (slot_num + slot_count)):
            slot_data = Slot('{}-{}-{}-{}-{}'.format(room, day_code, i, capacity, type), False)
            self.data[slot_key] = slot_data
            self.slots_used = self.slots_used + 1
            slot_block.append(slot_data)
          break
      else:
        if base_slot_check and availablitiy_slot_check:
          slot.available = False
          for i in range(slot_num, (slot_num + slot_count)):
            slot_data = Slot('{}-{}-{}-{}-{}'.format(room, day_code, i, capacity, type), False)
            self.data[slot_key] = slot_data
            self.slots_used = self.slots_used + 1
            slot_block.append(slot_data)
          break
    
    return slot_block
  
  
  def _generate_data(self, rooms):
    '''Generates set of available slots from list of rooms'''
    slots = {}
    
    for room_key, room in rooms:
      for slot in range(1, SLOTS_PER_DAY):
        for day in DAY_LIST:
          slot_key = '{}-{}-{}-{}-{}'.format(room['room'], day, slot, room['capacity'], room['type'])
          slots[slot_key] = Slot(slot_key, True)
          
    return slots
    
    
class Slot(object):
  '''
  An object that represents a single slot on the building schedule
  '''
  
  def __init__(self, data, available):
    '''Creates a single slot for the schedule'''
    self.data = data
    self.available = available