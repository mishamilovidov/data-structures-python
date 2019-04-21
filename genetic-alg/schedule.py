#!/usr/bin/env python3
import sys
import csv
import math
import random
from collections import namedtuple
from course_assignment import CourseAssignment
from slots import Slot

DayDetails = namedtuple('DayDetails', 'text code')
DAY_DETAILS = [
  DayDetails('monday', 'M'),
  DayDetails('tuesday', 'T'),
  DayDetails('wednesday', 'W'),
  DayDetails('thursday', 'Th'),
  DayDetails('friday', 'F'),
]
TOTAL_DAY_SLOTS = 18

class Schedule(object):
  '''
  An object to represent a complete schedule solution
  '''
  
  def __init__(self, rooms, slots, courses):
    '''Creates a schedule solution based on rooms available and classes to assign'''
    self.slots = slots
    self.rooms = rooms
    self.class_list = courses.data
    self.unused_rooms = []
    self.used_rooms = []
    self.courses_scheduled = []
    self.courses_not_scheduled = []
    self.number_of_students = self._calc_number_of_students()
    self.data = self._generate_data()
    
  def get_fitness(self):
    '''Calculates the fitness of the schedule solution'''
    avg_indv_fitness = self._calc_class_assignment_scores_sum() / len(self.data)
    
    # TODO: properly calculate free_time_blocks
    free_time_blocks = round(100 * self.slots.slots_used * 2 / self.slots.slots_used)
    students_outside_tnrb = round(100 * self._calc_students_outside_count() / self.number_of_students)
    unused_rooms = round(100 * len(self.unused_rooms) / 32)
    fitness = (0.6 * avg_indv_fitness) + (0.2 * free_time_blocks) - (0.2 * students_outside_tnrb) + (0.2 * unused_rooms)
    
    return round(fitness)
    
  def crossover(self, other_solution):
    '''Crosses with another scheudled solution and returns a new schedule solution'''
    
    
  def mutate(self):
    '''Mutates the schedule solution in some way'''
    
    
  def _calc_class_assignment_scores_sum(self):
    '''Calculates the sum of each class assignment fitness'''
    class_assignment_scores = []
    
    for assignment in self.data:
      class_assignment_scores.append(assignment.get_fitness())
      
    return sum(class_assignment_scores)
    
  
  def _calc_students_outside_count(self):
    '''Calculates students outside TNRB count'''
    students_outside_count = 0
    
    for course in self.courses_not_scheduled:
      students_outside_count = students_outside_count + int(course['students_per_section'])
      
    return students_outside_count
  
  def _generate_data(self):
    '''Generates a schedule solution'''
    data = []
    class_list = self.class_list
    unused_rooms = []
    used_rooms = []
    courses_scheduled = []
    courses_not_scheduled = []
    random.shuffle(class_list)
    
    for key, room in self.rooms:
      unused_rooms.append(room)
      
    not_scheduled = 0
    
    for course in class_list:
      course_room = None
      days = list(filter(None, [d.code if course[d.text] == 'x' else None for d in DAY_DETAILS]))
      min_capacity = int(course['students_per_section'])
      slot_count = int(course['slots'])
      course_slots = self.slots.get_free_slots(days, slot_count, min_capacity)
      
      if len(course_slots) == 0:  
        courses_not_scheduled.append(course)
      else:
        courses_scheduled.append(course)
        course_room = self.rooms.data[course_slots[0].data.split('-')[0]]
        
        if course_room not in used_rooms:
          used_rooms.append(course_room)
        
        if course_room in unused_rooms:
          unused_rooms.remove(course_room)
        
        data.append(CourseAssignment(course, course_room, course_slots))
        
    self.used_rooms = used_rooms
    self.unused_rooms = unused_rooms
    self.courses_scheduled = courses_scheduled
    self.courses_not_scheduled = courses_not_scheduled
    
    return data

  def _calc_number_of_students(self):
    '''Calculates the number of students based on the class list'''
    student_count_list = []
    
    for class_item in self.class_list:
      student_count_list.append(int(class_item['students_per_section']))
      
    return sum(student_count_list)
  
    