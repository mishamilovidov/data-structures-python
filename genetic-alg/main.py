#!/usr/bin/env python3
import sys
import csv
from rooms import Rooms
from slots import Slots
from schedule import Schedule

ROOMS_CSV = 'rooms.csv'
CLASSES_CSV = 'classes.csv'

def main():
  solution_fitness_items = []
  
  for i in range(1, 30):
    rooms = Rooms(ROOMS_CSV)
    slots = Slots(rooms)
    schedule = Schedule(rooms, slots, CLASSES_CSV)
    solution_fitness_items.append(schedule.get_fitness())
    print('{} solutions created'.format(i))

  print('AVERAGE FITNESS: {}'.format(sum(solution_fitness_items) / len(solution_fitness_items)))

### Main runner ###
if __name__ == '__main__':
    main()