#!/usr/bin/env python3
import sys
from collections import namedtuple

ScoreRange = namedtuple('ScoreRange', 'score min max')
CAPACITY_SCORES = [
  ScoreRange(50, 0, 5),
  ScoreRange(40, 6, 10),
  ScoreRange(30, 11, 15),
  ScoreRange(20, 16, 20),
  ScoreRange(10, 21, 25),
  ScoreRange(0, 26, None),
]

TimeRange = namedtuple('TimeRange', 'time_of_day min max')
COURSE_TIME_RANGES = [
  TimeRange('Morning', 1, 8),
  TimeRange('Afternoon', 9, 18)
]

class ClassAssignment(object):
  '''
  An object to represent a single course+room+time assignment on the schedule
  '''
  
  def __init__(self, course, room, slots):
    '''Creates a dictionary for a course assignment on the schedule'''
    self.course = course
    self.room = room
    self.time = slots
    
  
  def get_fitness(self):
    '''Calculates the fitness of a course assignment on the scheduled'''
    capacity_value = self._calc_capacity_score()
    pref_time_value = self._calc_time_score()
    pref_room_type_value = self._calc_room_type_score()
    
    return capacity_value + pref_time_value + pref_room_type_value;
    
    
  def _calc_capacity_score(self):
    '''Calculates the room capacity portion of the class assignment fitness score'''
    capacity_diff = int(self.room['capacity']) - int(self.course['students_per_section'])
    
    if capacity_diff < 0:
      score = 0
    else:
      for score_range in CAPACITY_SCORES:
        if not score_range.max:
          if capacity_diff >= score_range.min:
            score = score_range.score
            break
        else:
          if capacity_diff >= score_range.min and capacity_diff <= score_range.max:
            score = score_range.score
            break
    
    return score
  
  def _calc_room_type_score(self):
    '''Calculates the room type portion of the class assignment fitness score'''
    return 25 if self.room['type'] == self.course['preferred_room_type'] else 0
    
    
  def _calc_time_score(self):
    '''Calculates the time portion of the class assignment fitness score'''
    course_pref_time = self.course['preferred_time']
    time_list = list(self.time)
    start_time_num = time_list[0].split('-')[2]
    end_time_num = time_list[len(time_list)-1].split('-')[2]
    start_time_of_day = self._get_time_of_day(int(start_time_num))
    end_time_of_day = self._get_time_of_day(int(end_time_num))
        
    if start_time_of_day == course_pref_time and end_time_of_day == course_pref_time:
      score = 25
    elif start_time_of_day == course_pref_time and end_time_of_day != course_pref_time:
      score = 15
    elif start_time_of_day != course_pref_time and end_time_of_day == course_pref_time:
      score = 15
    else:
      score = 0

    return score

  
  def _get_time_of_day(self, time_num):
    '''Determines time of day for given time number slot'''    
    for time_range in COURSE_TIME_RANGES:
      if time_num >= time_range.min and time_num <= time_range.max:
        time_of_day = time_range.time_of_day
        
        return time_of_day