#!/usr/bin/env python3

class Array(object):
  '''
  An array implementation that holds arbitrary objects.
  '''

  def __init__(self, initial_size=10, chunk_size=5):
    '''Creates an array with an intial size.'''
    self.data = alloc(initial_size)
    self.size = 0
    self.chunk_size = chunk_size


  def debug_print(self):
    '''Prints a representation of the entire allocated space, including unused spots.'''
    print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))


  def _check_bounds(self, index):
    '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
    return True if (int(index) >= 0 and int(index) <= self.size - 1) else False

  def _check_increase(self):
    '''
    Checks whether the array is full and needs to increase by chunk size
    in preparation for adding an item to the array.
    '''
    return False if ((self.size + 1) <= len(self.data)) else True


  def _check_decrease(self):
    '''
    Checks whether the array has too many empty spots and can be decreased by chunk size.
    If a decrease is warranted, it should be done by allocating a new array and copying the
    data into it (don't allocate multiple arrays if multiple chunks need decreasing).
    '''
    remove_chunk = ((self.size - 1) % self.chunk_size) == 0
    
    return True if remove_chunk else False
  

  def add(self, item):
    '''Adds an item to the end of the array, allocating a larger array if necessary.'''    
    if self._check_increase():
      size = len(self.data) + self.chunk_size
      data = memcpy(alloc(size), self.data, len(self.data))
    else:
      size = len(self.data)
      data = memcpy(alloc(size), self.data, len(self.data))
    
    for index, i in enumerate(data):
      if i is None:
        data[index] = item
        break
    
    self.data = data 
    self.size = self.size + 1


  def insert(self, index, item):
    '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
    try:
      if self._check_bounds(index):
        if self._check_increase():
          size = len(self.data) + self.chunk_size
          data = memcpy(alloc(size), self.data, len(self.data))
        else:
          size = len(self.data)
          data = memcpy(alloc(size), self.data, len(self.data))
        
        for idx, i in enumerate(data):
          if i is None:
            data[idx] = data[idx - 1]
            break
          
        for i in range((len(data) - 1), int(index), -1) :
          data[i] = data[i - 1]
          
        for idx, i in enumerate(data):
          if i is None:
            data[idx - 1] = None
            break
            
        data[int(index)] = item
        
        self.data = data
        self.size = self.size + 1
      else:
        raise ValueError
    except ValueError:
      print('Error: {} is not within the bounds of the current array.'.format(index))

  def set(self, index, item):
    '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
    try:
      if self._check_bounds(index):
        self.data[int(index)] = item
      else:
        raise ValueError
    except ValueError:
      print('Error: {} is not within the bounds of the current array.'.format(index))

  def get(self, index):
    '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
    try:
      if self._check_bounds(index):
        print(self.data[int(index)])
      else:
        raise ValueError
    except ValueError:
      print('Error: {} is not within the bounds of the current array.'.format(index))

  def delete(self, index):
    '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
    try:
      if self._check_bounds(index):
        if self._check_decrease():
          data = alloc(len(self.data) - self.chunk_size)
        else:
          data = alloc(len(self.data))
          
        for i in range(int(index)):
          data[i] = self.data[i]
          
        for i in range(int(index), (self.size - 1)):
          data[i] = self.data[i+1]
        
        self.data = data
        self.size = self.size - 1
      else:
        raise ValueError
    except ValueError:
      print('Error: {} is not within the bounds of the current array.'.format(index))

  def swap(self, index1, index2):
    '''Swaps the values at the given indices.'''
    try:
      if not self._check_bounds(index1):
        raise ValueError(index1)    
      elif not self._check_bounds(index2):
        raise ValueError(index2)
      else:
        data = memcpy(alloc(len(self.data)), self.data, len(self.data))
        
        self.data[int(index1)] = data[int(index2)]
        self.data[int(index2)] = data[int(index1)]
    except ValueError as index:
      print('Error: {} is not within the bounds of the current array.'.format(index))

###################################################
###   Utilities

def alloc(size):
  '''
  Allocates array space in memory. This is similar to C's alloc function.
  '''
  data = []
  for i in range(size):
      data.append(None)
  return data


def memcpy(dest, source, size):
  '''
  Copies items from one array to another.  This is similar to C's memcpy function.
  '''
  for i in range(size):
    dest[i] = source[i]
  return dest