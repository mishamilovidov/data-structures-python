#!/usr/bin/env python3
import os, os.path, binascii, re
from collections import namedtuple
from io import StringIO


# a named tuple to hold an individual key and value
# this Node "object" is never seen outside this class
# (e.g. get() returns the value, not the full Node)
Node = namedtuple("Node", ( 'key', 'value' ))

# This is super small because we want to test the loading and print for debugging easier
NUM_BUCKETS = 10


class Hashtable(object):
    '''
    An abstract hashtable superclass.
    '''
    def __init__(self):
        self.buckets = []
        for index in range(0, NUM_BUCKETS):
          self.buckets.append([])

    def set(self, key, value):
        '''
        Adds the given key=value pair to the hashtable.
        '''
        node = Node(key, value)
        indexNumber = self.get_bucket_index(key)
        self.buckets[indexNumber].append(node)

    def get(self, key):
        '''
        Retrieves the value under the given key.
        Returns None if the key does not exist.
        '''
        indexNumber = self.get_bucket_index(key)
        value = None;
        
        for node in self.buckets[indexNumber]:
          if node.key == key:
            value = node.value

        return value;

    def remove(self, key):
        '''
        Removes the given key from the hashtable.
        Returns silently if the key does not exist.
        '''
        indexNumber = self.get_bucket_index(key)
        
        for index, node in enumerate(self.buckets[indexNumber]):
          if node.key == key:
            del self.buckets[indexNumber][index]


    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        # leave this method as is - write your code in the subclasses
        raise NotImplementedError('This method is abstract!  The subclass must define it.')



    ##################################################
    ###   Helper methods

    def __repr__(self):
        '''Returns a representation of the hash table'''
        buf = StringIO()
        for i, bkt in enumerate(self.buckets):
            for j, node in enumerate(bkt):
                buf.write('{:>5}  {}\n'.format(
                    '[{}]'.format(i) if j == 0 else '',
                    node.key,
                ))
        return buf.getvalue()



######################################################
###   String hash table

class StringHashtable(Hashtable):
    '''A hashtable that takes string keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''        
        return sum([ord(char) - 96 for char in key.replace(' ','')]) % NUM_BUCKETS;



######################################################
###   Guid hash table

COUNTER_CHARS = ( 16, 24 )

class GuidHashtable(Hashtable):
    '''A hashtable that takes GUID keys'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        return int(key[COUNTER_CHARS[0]:COUNTER_CHARS[1]], 16) % NUM_BUCKETS;



######################################################
###   Image hash table

NUM_CHUNKS = 8

class ImageHashtable(Hashtable):
    '''A hashtable that takes image name keys and creates the hash from (some of) the bytes of the file.'''

    def get_bucket_index(self, key):
        '''
        Returns the bucket index number for the given key.
        The number will be in the range of the number of buckets.
        '''
        #TODO: hash the string and return the bucket index that should be used
        return 0;
