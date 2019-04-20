#!/usr/bin/env python3
import sys
import csv
from available_slots import AvailableSlots
from schedule_solution import ScheduleSolution

ROOMS_CSV = 'rooms.csv'
CLASSES_CSV = 'classes.csv'

def main():
  slots = AvailableSlots(ROOMS_CSV)
  solution = ScheduleSolution(slots, CLASSES_CSV)
  
  print(len(solution.class_list))

### Main runner ###
if __name__ == '__main__':
    main()