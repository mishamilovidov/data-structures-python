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
        return True if (int(index) >= 0 and int(index) <= self.size - 1) else False


    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        n = Node(item)
        if self.head is None:
            self.head = n
            self.size = 1
        else:
            last_item = self.head
            
            while last_item.next != None:
                last_item = last_item.next
            
            last_item.next = n
            self.size = self.size + 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        try:
            if self._get_node(index):
                n = Node(item)
                t = self.head
                counter = 1

                while t != None:
                    if int(index) == counter:
                        n.next = t.next
                        t.next = n
                        self.size = self.size + 1
                        break
                    counter = counter + 1
                    t = t.next
            else:
                raise ValueError
        except ValueError:
          print('Error: {} is not within the bounds of the current array.'.format(index))
          return 'Error: {} is not within the bounds of the current array.'.format(index)

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        try:
            if self._get_node(index):
                t = self.head
                counter = 0

                while t != None:
                    if int(index) == counter:
                        t.value = item
                        break
                    counter = counter + 1
                    t = t.next
            else:
                raise ValueError
        except ValueError:
          print('Error: {} is not within the bounds of the current array.'.format(index))
          return 'Error: {} is not within the bounds of the current array.'.format(index)


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        try:
            if self._get_node(index):
                t = self.head
                counter = 0
                
                while t != None:
                    if int(index) == counter:
                        print(t.value)
                        break
                    counter = counter + 1
                    t = t.next
            else:
                raise ValueError
        except ValueError:
            print('Error: {} is not within the bounds of the current array.'.format(index))
            return 'Error: {} is not within the bounds of the current array.'.format(index)

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        try:
            if self._get_node(index):
                p = None
                t = self.head
                counter = 0

                while t != None:
                    if int(index) == counter:
                        p.next = t.next
                        t = None
                        self.size = self.size - 1
                        break
                    counter = counter + 1
                    p = t
                    t = t.next
            else:
                raise ValueError
        except ValueError:
          print('Error: {} is not within the bounds of the current array.'.format(index))
          return 'Error: {} is not within the bounds of the current array.'.format(index)


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        try:
            if not self._get_node(index1):
                raise ValueError(index1)    
            elif not self._get_node(index2):
                raise ValueError(index2)
            else:
                p1 = None
                t1 = self.head 
                counter1 = 0
                while t1 != None and counter1 != int(index1): 
                    p1 = t1 
                    t1 = t1.next
                    counter1 = counter1 + 1
          
                p2 = None
                t2 = self.head 
                counter2 = 0
                while t2 != None and counter2 != int(index2): 
                    p2 = t2 
                    t2 = t2.next
                    counter2 = counter2 + 1
          
                if p1 != None: 
                    p1.next = t2
                else:
                    self.head = t2
  
                if p2 != None: 
                    p2.next = t1 
                else: 
                    self.head = t1
          
                temp = t1.next
                t1.next = t2.next
                t2.next = temp 
        except ValueError as index:
            print('Error: {} is not within the bounds of the current array.'.format(index))
            return 'Error: {} is not within the bounds of the current array.'.format(index)


######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
