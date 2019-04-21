#!/usr/bin/env python3
import sys
import copy
import csv
import math
import numpy as np
import pprint
from rooms import Rooms
from slots import Slots
from courses import Courses
from schedule import Schedule

ROOMS_CSV = 'rooms.csv'
CLASSES_CSV = 'classes.csv'

class Generation(object):
  '''
  An object to represent a generation schedule solutions
  '''
  
  def __init__(self, population, elite, crossover, mutate, data=None):
    '''Creates a generation of schedule solutions '''
    self.avg_solution_fitness = 0
    self.population = population
    self.elite_amount = elite
    self.crossover_amount = crossover
    self.mutate_amount = mutate
    self.elites = []
    self.crossover = []
    self.mutations = []
    self.untouched = []
    self.data = self._generate_data(data)
    
  def _generate_data(self, data):
    '''Generate data for the generation'''
    solution_fitness_items = []
    solution_items = {}
    solutions = []
    
    for i in range(0, self.population):
      rooms = Rooms(ROOMS_CSV)
      slots = Slots(rooms)
      courses = Courses(CLASSES_CSV)
      schedule = data[i] if data else Schedule(rooms, slots, courses)
        
      solutions.append(schedule)
      schedule_fitness = schedule.get_fitness()
      solution_fitness_items.append(schedule_fitness)
      solution_fitness_items.sort()
      
      if schedule_fitness in solution_items.keys():
        solution_items[schedule_fitness][schedule.id] = schedule
      else:
        solution_items[schedule_fitness] = {}
        solution_items[schedule_fitness][schedule.id] = schedule
  
    self.elites = self._generate_elite_list(solution_items)
    self.avg_solution_fitness = round(sum(solution_fitness_items) / len(solution_fitness_items))
    return solutions
    
    
  def _generate_elite_list(self, solution_items):
    '''Iterates over solutions in generation and determines elites'''
    temp_solution_items = copy.deepcopy(solution_items)
    elite_count = math.ceil(self.population * self.elite_amount)
    elites = []
    
    for key in reversed(sorted(solution_items)):
      if len(elites) == elite_count:
          break
          
      for item in solution_items[key]:
        elites.append(solution_items[key][item])
        del temp_solution_items[key][item]
        
        if len(elites) == elite_count:
          break
    
    self.crossovers = self._generate_crossover_list(temp_solution_items)
    return elites
    
    
  def _generate_crossover_list(self, solution_items):
    '''Iterates over solutions in generation and creates list of solutions for crossovers'''
    temp_solution_items = copy.deepcopy(solution_items)
    crossover_count = math.floor(self.population * self.crossover_amount)
    crossovers = []
    
    for key in solution_items:
      if len(crossovers) == crossover_count:
        break
        
      for item in solution_items[key]:
        crossovers.append(solution_items[key][item])
        del temp_solution_items[key][item]
        
        if len(crossovers) == crossover_count:
          break
    
    self.mutations = self._generate_mutation_list(temp_solution_items)
    return crossovers
    
    
  def _generate_mutation_list(self, solution_items):
    '''Iterates over solutions in generation and creates list of solutions for mutations'''
    temp_solution_items = copy.deepcopy(solution_items)
    mutation_count = math.floor(self.population * self.mutate_amount)
    mutations = []
    
    for key in solution_items:
      if len(mutations) == mutation_count:
        break
        
      for item in solution_items[key]:
        mutations.append(solution_items[key][item])
        del temp_solution_items[key][item]
        
        if len(mutations) == mutation_count:
          break
    
    self.untouched = self._generate_untouched_list(temp_solution_items)
    return mutations
    
    
  def _generate_untouched_list(self, solution_items):
    '''Iterates over the remaining solutions and creates a list of untouched solutions'''
    untouched = []
    
    for key in solution_items:
      for item in solution_items[key]:
        untouched.append(solution_items[key][item])
        
    return untouched