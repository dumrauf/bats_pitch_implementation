from unittest import TestCase

__author__ = 'Dominic Dumrauf'


class DataTypesTestCase(TestCase):
    def _test_invalid_length(self, valid_length, valid_char, data_type):
        too_small = range(valid_length)
        too_big = range(valid_length + 1, valid_length + 100)
        for i in too_big + too_small:
            self.assertFalse(data_type.is_valid(valid_char * i))
