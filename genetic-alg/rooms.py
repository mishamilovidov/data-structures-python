#!/usr/bin/env python3
import sys
import csv
import random

class Rooms(object):
  '''
  An object that represents the available rooms for the building schedule
  '''
  
  def __init__(self, rooms_csv):
    '''Creates a set for the available slots on a schedule'''
    self.data = self._generate_data(rooms_csv)


  def __iter__(self):
    '''Iterates through the linked list, implemented as a generator.'''
    for key, value in self.data.items():
      yield (key, value)
  
  
  def _generate_data(self, rooms_csv):
    '''Generates dictionary of rooms from csv data'''
    rooms_info = []
    rooms = {}
    room_attributes = []
    
    with open(rooms_csv) as input_file:
      csv_reader = csv.reader(input_file, delimiter=',')
      for row in csv_reader:
        rooms_info.append(row)
        
    for item in rooms_info[0]:
      room_attributes.append(item.strip().lower().replace(' ','_'))
    
    rooms_info.remove(rooms_info[0])
    random.shuffle(rooms_info)
    
    for row in rooms_info:
      room = {}
      for index, item in enumerate(row):
        room[room_attributes[index]] = item
      rooms[room['room']] = room
          
    return rooms