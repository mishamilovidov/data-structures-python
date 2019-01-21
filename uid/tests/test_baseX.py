from unittest import TestCase
from baseX import BaseXConverter

# Run this from its parent directory:
#
#    python3 -m unittest tests/test_baseX
#

class BaseXTester(TestCase):

    def test_base2(self):
        conv = BaseXConverter('01')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0b}'.format(i))
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_base8(self):
        conv = BaseXConverter('01234567')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0o}'.format(i))
        self.assertEqual(i, conv.invert(conv.convert(i)))

    def test_base16(self):
        conv = BaseXConverter('0123456789ABCDEF')
        i = 1234567890
        self.assertEqual(conv.convert(i), '{:0x}'.format(i).upper())
        self.assertEqual(i, conv.invert(conv.convert(i)))

    # def test_base58(self):
    #     conv = BaseXConverter('01')
    #     i = 1234567890
    #     self.assertEqual(conv.convert(i), '{:0b}'.format(i))
    #     self.assertEqual(i, conv.invert(conv.convert(i)))
    #
    # def test_base64(self):
    #     conv = BaseXConverter('01')
    #     i = 1234567890
    #     self.assertEqual(conv.convert(i), '{:0b}'.format(i))
    #     self.assertEqual(i, conv.invert(conv.convert(i)))
