#!/usr/bin/env python3
import sys
from generation import Generation

POPULATION = 10
ELITE = 0.05
CROSSOVER = 0.8
MUTATE = 0.05

def print_run_info():
  print('\n')
  print('Population: {}'.format(POPULATION))
  print('Elite: {}%'.format(ELITE * 100))
  print('Crossover: {}%'.format(CROSSOVER * 100))
  print('Mutations: {}%'.format(MUTATE * 100))
  print('\n')
  print('Generation, SolutionFitValue')

def main():
  print_run_info()
  generation = Generation(POPULATION, ELITE, CROSSOVER, MUTATE)
  generation_avg_fitness_list = [ generation.avg_solution_fitness ]
  run_count = 1
  
  print('{}, {}'.format(run_count, generation.avg_solution_fitness))

  for i in range(1, 3):
    solution_data = []
    solution_data = solution_data + generation.elites + generation.untouched
    mutated_solutions = []
    crossedover_solutions = []
    
    for item in generation.mutations:
      mutated_solutions.append(item.mutate())
      
    for i in range(0, int(len(generation.crossovers) / 2)):
      item = generation.crossovers[i]
      other_item = generation.crossovers[len(generation.crossovers) - i - 1]
      
      for new_item in item.crossover(other_item):
        crossedover_solutions.append(new_item)
            
    solution_data = solution_data + mutated_solutions + crossedover_solutions
    generation = Generation(POPULATION, ELITE, CROSSOVER, MUTATE, solution_data)
    run_count = run_count + 1
    generation_avg_fitness_list.append(generation.avg_solution_fitness)
    print('{}, {}'.format(run_count, generation.avg_solution_fitness))

### Main runner ###
if __name__ == '__main__':
    main()