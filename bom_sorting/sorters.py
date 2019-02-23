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


def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    data.sort(key=lambda t: t[index], reverse=descending)


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    data.sort(key=lambda t: t[index], reverse=descending)


def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    data.sort(key=lambda t: t[index], reverse=descending)
