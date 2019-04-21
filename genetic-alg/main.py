#!/usr/bin/env python3
import sys
import csv
from rooms import Rooms
from slots import Slots
from courses import Courses
from schedule import Schedule

ROOMS_CSV = 'rooms.csv'
CLASSES_CSV = 'classes.csv'

def main():
  solution_fitness_items = []
  
  for i in range(1, 30):
    rooms = Rooms(ROOMS_CSV)
    slots = Slots(rooms)
    courses = Courses(CLASSES_CSV)
    schedule = Schedule(rooms, slots, courses)
    
    solution_fitness_items.append(schedule.get_fitness())
    print('{} solutions created'.format(i))

  avg_solution_fitness = round(sum(solution_fitness_items) / len(solution_fitness_items))
  print('AVERAGE FITNESS: {}'.format(avg_solution_fitness))

### Main runner ###
if __name__ == '__main__':
    main()