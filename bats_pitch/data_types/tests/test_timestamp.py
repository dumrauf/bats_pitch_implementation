from unittest import TestCase
from bats_pitch.data_types.tests.mixins import DataTypesTestCase
from bats_pitch.data_types.timestamp import Timestamp

__author__ = 'Dominic Dumrauf'


class NumericTest(DataTypesTestCase, TestCase):
    def setUp(self):
        self.t = Timestamp(length=8)

    def test_valid_timestamp(self):
        self.assertTrue(self.t.is_valid('00000000'))
        self.assertTrue(self.t.is_valid('00000001'))
        self.assertTrue(self.t.is_valid('10000000'))
        self.assertTrue(self.t.is_valid('01234567'))
        self.assertTrue(self.t.is_valid('12345678'))

    def test_invalid_timestamp_wrong_base_set(self):
        self.assertFalse(self.t.is_valid('        '))
        self.assertFalse(self.t.is_valid('0000000i'))
        self.assertFalse(self.t.is_valid('0invalid'))
        self.assertFalse(self.t.is_valid('notvalid'))
        self.assertFalse(self.t.is_valid('NOTVALID'))

    def test_invalid_timestamp_wrong_length(self):
        self._test_invalid_length(valid_length=self.t.length,
                                  valid_char='0',
                                  data_type=self.t)
