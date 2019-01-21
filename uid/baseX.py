#!/usr/bin/env python3

class BaseXConverter(object):
    '''
    Converts positive, base-10 numbers to base-X numbers using a custom alphabet.
    The base is given by the length of the alphabet specified in the constructor.
    The first character in the alphabet has a value of zero,
    the second character a value of one, and so forth.

    Examples:
        Base2:  BaseXConverter('01')
        Base2:  BaseXConverter('<>')     # custom alphabet: < is a zero value and > is a one value
        Base4:  BaseXConverter('0123')
        Base20: BaseXConverter('0123456789abcdefghij')

    See the unit tests at the bottom of the file for many examples.
    '''

    def __init__(self, alphabet):
        '''
        The base is taken from the number of characters in the alphabet.
        '''
        self.alphabet = list(alphabet)
        self.base = len(alphabet)
        self.alphabet_index = {
          val:index
          for index,val in enumerate(self.alphabet)
            if index < self.base
        }

    def convert(self, val):
        '''
        Converts value from base 10 to base X.
        The return value is a baseX integer, wrapped as a string.
        '''
        if val == 0:
          return digs[0]

        digits = []

        while val:
          digits.append(self.alphabet[int(val % self.base)])
          val = int(val / self.base)

        if sign < 0: digits.append('-')
        digits.reverse()
        bXval = ''.join(digits)

        return bXval

    def invert(self, bXval):
        '''
        Converts a value from base X to base 10.
        The bXval should be a baseX integer, wrapped as a string.
        Raises a ValueError if bXval contains any chars not in the alphabet.
        '''
        val = 0
        for digit in bXval:
          try:
            val = val*self.base + self.alphabet_index[digit]
          except KeyError:
            if digit in self.alphabet:
              raise ValueError("invalid char '{}' in base {}".format(digit, self.base))

        return val
