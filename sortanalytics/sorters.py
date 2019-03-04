# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#
import operator

def bubble_sort(data, index, descending=False):
  '''Sorts using the bubble sort algorithm'''
  lessThan = operator.lt
  greaterThan = operator.gt
  comp = lessThan if descending else greaterThan
  
  for pass_count in range(len(data)-1, 0, -1):
    for i in range(pass_count):
      if comp(data[i][index], data[i+1][index]):
        temp = data[i]
        data[i] = data[i+1]
        data[i+1] = temp
    
  return data

def insertion_sort(data, index, descending=False):
  '''Sorts using the insertion sort algorithm'''
  lessThan = operator.lt
  greaterThan = operator.gt
  comp = lessThan if descending else greaterThan
  
  for i in range(1, len(data)):
    current = data[i]
    position = i
    
    while position > 0 and comp(data[position - 1][index], current[index]):
      data[position] = data[position-1]
      position = position-1
    
    data[position] = current
      
  return data


def selection_sort(data, index, descending=False):
  '''Sorts using the selection sort algorithm'''
  lessThan = operator.lt
  greaterThan = operator.gt
  comp = lessThan if descending else greaterThan
  
  for i in range(len(data)-1, 0, -1):
    max_position = 0
    
    for position in range(1, i + 1):
      if comp(data[position][index], data[max_position][index]):
         max_position = position

    temp = data[i]
    data[i] = data[max_position]
    data[max_position] = temp

  return data


def quick_sort(data, index, descending=False):
    '''Sorts using the quick sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    # data.sort(key=lambda t: t[index], reverse=descending)
    def partition(data, first, last):
      # define pivot value
      pivot = data[first][index]
    
      # define initial left and right points
      left_point = first+1
      right_point = last
    
      done = False
      while not done:
        while left_point <= right_point and data[left_point][index] <= pivot:
          left_point = left_point + 1
        
        while data[right_point][index] >= pivot and right_point >= left_point:
          right_point = right_point -1
        
        # once the indices cross, stop looping because of arriving at pivot
        if right_point < left_point:
          done = True
        # otherwise, swap the values at the indices 
        else:
          temp = data[left_point]
          data[left_point] = data[right_point]
          data[right_point] = temp
      
      # swap values at pivot point
      temp = data[first]
      data[first] = data[right_point]
      data[right_point] = temp
      
      return right_point
        
    def inner(data, low, high):
      if low < high:
        split_index = partition(data, low, high)
        
        inner(data, low, split_index-1)
        inner(data, split_index+1, high)
        
    first = 0
    last = len(data)-1
    inner(data, first, last)


def python_sort(data, index, descending=False):
    '''Sorts using the native Python sort algorithm (Timsort)'''
    # LEAVE this function as is - it will allow you to see your sorts against the python one
    data.sort(key=lambda t: t[index], reverse=descending)
