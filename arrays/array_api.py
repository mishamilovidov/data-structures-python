#!/usr/bin/env python3


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = alloc(initial_size)
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''


    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''


    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''


    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''


    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''




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
