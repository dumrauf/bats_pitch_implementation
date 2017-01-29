from unittest import TestCase
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.data_types.tests.mixins import DataTypesTestCase

__author__ = 'Dominic Dumrauf'


class NumericTest(DataTypesTestCase, TestCase):
    def setUp(self):
        self.n = Numeric(length=8)

    def test_valid_numeric(self):
        self.assertTrue(self.n.is_valid('00000000'))
        self.assertTrue(self.n.is_valid('00000001'))
        self.assertTrue(self.n.is_valid('10000000'))
        self.assertTrue(self.n.is_valid('01234567'))
        self.assertTrue(self.n.is_valid('12345678'))

    def test_invalid_numeric_wrong_base_set(self):
        self.assertFalse(self.n.is_valid('        '))
        self.assertFalse(self.n.is_valid(' 1234567'))
        self.assertFalse(self.n.is_valid('0000000i'))
        self.assertFalse(self.n.is_valid('0invalid'))
        self.assertFalse(self.n.is_valid('notvalid'))
        self.assertFalse(self.n.is_valid('NOTVALID'))

    def test_invalid_numeric_wrong_length(self):
        self._test_invalid_length(valid_length=self.n.length,
                                  valid_char='0',
                                  data_type=self.n)
