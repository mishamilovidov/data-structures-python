#!/usr/bin/env python3
import sys
import csv
from linkedlist_api import LinkedList

FILE_INPUT = 'data.csv'
# FILE_OUTPUT = 'output.txt'
COMMANDS = {
  'CREATE': { 'method': '', 'param_count': 0 },
  'DEBUG': { 'method': 'debug_print', 'param_count': 0 },
  'ADD': { 'method': 'add', 'param_count': 1 },
  'SET': { 'method': 'set', 'param_count': 2 },
  'GET': { 'method': 'get', 'param_count': 1 },
  'DELETE': { 'method': 'delete', 'param_count': 1 },
  'INSERT': { 'method': 'insert', 'param_count': 2 },
  'SWAP': { 'method': 'swap', 'param_count': 2 },
}

def exec_command(command, linkedlist, param_one, param_two):
  method = COMMANDS[command]['method']
  param_count = COMMANDS[command]['param_count']

  if param_count == 2:
    getattr(LinkedList, method)(linkedlist, param_one, param_two) 
  elif param_count == 1:
    getattr(LinkedList, method)(linkedlist, param_one) 
  else:
    getattr(LinkedList, method)(linkedlist)  

def main():
  with open(FILE_INPUT) as input_file:
    # with open(FILE_OUTPUT, 'w') as output_file:
      # sys.stdout = output_file
    csv_reader = csv.reader(input_file, delimiter=',')
    line = 0
    
    for row in csv_reader:
      command = row[0]
      param_one = row[1]
      param_two = row[2]
    
      # print line number and command
      print('{}:{},{},{}'.format(line, command, param_one, param_two))
      
      # call appropriate method based on command
      if command == 'CREATE':
        linkedlist = LinkedList()
      else:
        exec_command(command, linkedlist, param_one, param_two)

      line += 1
    
if __name__ == '__main__':
  main()
  