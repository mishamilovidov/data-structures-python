#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire list.'''
        print('{} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ])))
        return '{} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ]))


    def __iter__(self):
        '''Iterates through the linked list, implemented as a generator.'''
        for node in self._iter_nodes():
            yield node.value


    def _iter_nodes(self):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current
            current = current.next


    def _get_node(self, index):
      '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
      if (int(index) >= 0 and int(index) <= self.size - 1):
        for counter, node in enumerate(self._iter_nodes()):
          if counter == index:
            return node
      else:
        raise ValueError('Error: {} is not within the bounds of the current array.'.format(index))


    def add(self, item):
      '''Adds an item to the end of the linked list.'''
      n = Node(item)
      if self.head is None:
        self.head = n
        self.size = 1
      else:
        try:
          # get the last item in the list
          last_item = self._get_node(self.size - 1)
          
          # point last item to new last item
          last_item.next = n
          
          # increase size of list
          self.size = self.size + 1
        except Exception as e:
          print(e)
          return e


    def insert(self, index, item):
      '''Inserts an item at the given index, shifting remaining items right.'''
      try:
        # create new node
        new = Node(item)
        
        # get previous and current nodes relative to index
        prev = self._get_node(int(index) - 1)
        curr = prev.next
        
        # change pointer to insert new node
        new.next = curr
        prev.next = new
        
        # increase size of list
        self.size = self.size + 1
      except Exception as e:
        print(e)
        return e


    def set(self, index, item):
      '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
      try:
        # get node at index
        new = self._get_node(int(index))
        
        # change the value at the index
        new.value = item
      except Exception as e:
        print(e)
        return e


    def get(self, index):
      '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
      try:
        # get node at index
        node = self._get_node(int(index))
        
        # print value of node
        print(node.value)
        return node.value
      except Exception as e:
        print(e)
        return e


    def delete(self, index):
      '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
      if int(index) == 0:
        node = self._get_node(int(index))
        self.head = node.next
        self.size = self.size - 1
      else:
        try:
          # get node at index and previous and next nodes
          node = self._get_node(int(index))
          prev = self._get_node(int(index) - 1)
          next = node.next
        
          # point previous node to next node
          prev.next = next
          node = None
          
          # decrease size of list
          self.size = self.size - 1
        except Exception as e:
          print(e)
          return e


    def swap(self, index1, index2):
      '''Swaps the values at the given indices.'''
      try:
        # get nodes at the two indices
        node1 = self._get_node(int(index1))
        node2 = self._get_node(int(index2))
        
        # change the values of the two indices
        temp = node1.value
        node1.value = node2.value
        node2.value = temp
      except Exception as e:
        print(e)
        return e


######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
