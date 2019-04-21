#!/usr/bin/env python3
import sys
import copy
import csv
import math
import pprint
import random
import uuid
from itertools import groupby
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
    self.id = uuid.uuid4().hex
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
    free_time_blocks = round(100 * self._calc_free_block_score() / len(self.slots.data))
    students_outside_tnrb = round(100 * self._calc_students_outside_count() / self.number_of_students)
    unused_rooms = round(100 * len(self.unused_rooms) / 32)
    fitness = (0.6 * avg_indv_fitness) + (0.2 * free_time_blocks) - (0.2 * students_outside_tnrb) + (0.2 * unused_rooms)
    
    return round(fitness)
    
    
  def crossover(self, other_solution):
    '''Crosses with another scheudled solution and returns two changed schedule solutions'''
    this_schedule = copy.deepcopy(self)
    other_schedule = copy.deepcopy(other_solution)
    
    # remove Monday/Wednesday course assignments from other_schedule
    for course_assignment in other_schedule.data:
      if course_assignment.course['monday'] == 'x' and course_assignment.course['wednesday'] == 'x':
        del other_schedule.data[other_schedule.data.index(course_assignment)]
    
    # add Monday/Wednesday course assignments from this_schedule to other_schedule
    for course_assignment in this_schedule.data:
      if course_assignment.course['monday'] == 'x' and course_assignment.course['wednesday'] == 'x':
        other_schedule.data.append(course_assignment)
    
    
    return (this_schedule, other_schedule)
    
    
  def mutate(self):
    '''Mutates a schedule solution in some way'''
    return self
    
    
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
    
    
  def _calc_free_block_score(self):
    '''Calulates the free block score across all rooms'''
    free_slots_dict = self._generate_free_slots_dict()
    free_block_scores_dict = self._generate_free_block_scores_dict(free_slots_dict)
    free_block_score = 0
    
    for r in free_block_scores_dict:
      for d in DAY_DETAILS:
        room_day_score = free_block_scores_dict[r][d.code]['free_block_score']
        free_block_score = free_block_score + int(room_day_score)
        
    return free_block_score
  
  
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
      pref_type = course['preferred_room_type'] 
      pref_time = course['preferred_time']
      min_capacity = int(course['students_per_section'])
      slot_count = int(course['slots'])
      course_slots = self.slots.get_free_slots(days, slot_count, min_capacity, pref_type, pref_time)
      
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
    
    
  def _get_unused_slots(self):
    '''Creates list of unused slots based on used_slots list'''
    slots_unused = self.slots.data
    
    for item in self.slots.slots_used:
      if item.data in slots_unused.keys():
        del slots_unused[item.data]
      
    return slots_unused
    
    
  def _generate_free_slots_dict(self):
    '''Generates a dictionary of the free slots after course assignemnt'''
    unused_slots_dict = {}
    
    for r in self.rooms.data:
      unused_slots_dict[r] = {}
      for d in DAY_DETAILS:
        unused_slots_dict[r][d.code] = {}
        unused_slots_dict[r][d.code]['slot_nums'] = []
            
    for slot in self._get_unused_slots():
      slot_attrs = slot.split('-')
      room = slot_attrs[0]
      day = slot_attrs[1]
      slot_num = int(slot_attrs[2])
      capacity = slot_attrs[3]
      type = slot_attrs[4]
      
      unused_slots_dict[room][day]['slot_nums'].append(slot_num)
      
    for r in unused_slots_dict:
      for d in DAY_DETAILS:
        slot_nums = unused_slots_dict[r][d.code]['slot_nums']
        slot_nums.sort()
        unused_slots_dict[r][d.code]['slot_nums'] = slot_nums
      
    return unused_slots_dict
    

  def _generate_free_block_scores_dict(self, free_slots_dict):
    '''Generates a dictionary with free block scores per room per day'''
    for r in free_slots_dict:
      for d in DAY_DETAILS:
        slot_nums = free_slots_dict[r][d.code]['slot_nums']
        slot_num_ranges = []
        
        for range in ranges(slot_nums):
          slot_num_ranges.append(range)
        
        free_slots_dict[r][d.code]['free_block_score'] = max(slot_num_ranges)
        
    return free_slots_dict
    

  def _calc_number_of_students(self):
    '''Calculates the number of students based on the class list'''
    student_count_list = []
    
    for class_item in self.class_list:
      student_count_list.append(int(class_item['students_per_section']))
      
    return sum(student_count_list)
  
def ranges(lst):
  '''Yields a generator with the range sizes in a list of ints'''
  pos = (j - i for i, j in enumerate(lst))
  t = 0
  for i, els in groupby(pos):
    l = len(list(els))
    yield l