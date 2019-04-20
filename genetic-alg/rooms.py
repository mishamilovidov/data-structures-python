#!/usr/bin/env python3
import sys
import csv

class Rooms(object):
  '''
  An object that represents the available rooms for the building schedule
  '''
  
  def __init__(self, rooms_csv):
    '''Creates a set for the available slots on a schedule'''
    self.data = self._generate_data(rooms_csv)


  def __iter__(self):
    '''Iterates through the linked list, implemented as a generator.'''
    for room in self.data:
        yield room
  
  
  def _generate_data(self, rooms_csv):
    '''Generates dictionary of rooms from csv data'''
    with open(rooms_csv) as input_file:
      room_list = []
      room_attributes = []
      csv_reader = csv.reader(input_file, delimiter=',')
      
      for idx, row in enumerate(csv_reader):
        if idx == 0:
          for item in row:
            room_attributes.append(item.strip().lower().replace(' ','_'))
        else:
          room = {}
          for index, item in enumerate(row):
            room[room_attributes[index]] = item
          room_list.append(room)
            
      return room_list