from unittest import TestCase
from bats_pitch.data_types.base_36_numeric import Base36Numeric
from bats_pitch.data_types.tests.mixins import DataTypesTestCase

__author__ = 'Dominic Dumrauf'


class Base36NumericTest(DataTypesTestCase, TestCase):
    def setUp(self):
        self.b = Base36Numeric(length=8)

    def test_valid_base_36_numeric(self):
        self.assertTrue(self.b.is_valid('00000000'))
        self.assertTrue(self.b.is_valid('00000001'))
        self.assertTrue(self.b.is_valid('000VALID'))
        self.assertTrue(self.b.is_valid('0VALID01'))
        self.assertTrue(self.b.is_valid('0VALID01'))
        self.assertTrue(self.b.is_valid('VALIDTOO'))

    def test_invalid_base_36_numeric_wrong_base_set(self):
        self.assertFalse(self.b.is_valid('notvalid'))
        self.assertFalse(self.b.is_valid('0invalid'))
        self.assertFalse(self.b.is_valid('invalid1'))
        self.assertFalse(self.b.is_valid('  VALID0'))
        self.assertFalse(self.b.is_valid('        '))

    def test_invalid_base_36_numeric_wrong_length(self):
        self._test_invalid_length(valid_length=self.b.length,
                                  valid_char='0',
                                  data_type=self.b)
