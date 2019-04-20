#!/usr/bin/env python3
import sys
import csv
from rooms import Rooms
from slots import Slots
from schedule import Schedule

ROOMS_CSV = 'rooms.csv'
CLASSES_CSV = 'classes.csv'

def main():
  rooms = Rooms(ROOMS_CSV)
  slots = Slots(rooms)
  schedule = Schedule(rooms, slots, CLASSES_CSV)
#   
#   room = {'room': '151', 'capacity': '45', 'type': 'Flat'}
#   course = {'section': 1, 'preferred_time': 'Morning', 'wednesday': 'x', 'friday': '', 'slots': 4, 'monday': 'x', 'preferred_room_type': 'Flat', 'hours': '1.75', 'thursday': '', 'tuesday': '', 'course': 'BUS M 582', 'students_per_section': '45'}
#   slots = { '151-M-4-344-Auditorium',  '151-M-5-344-Auditorium', '151-M-6-344-Auditorium', '151-M-7-344-Auditorium'}
  
  class_assignment = ClassAssignment(course, room, slots)

### Main runner ###
if __name__ == '__main__':
    main()