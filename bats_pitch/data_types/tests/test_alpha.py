from unittest import TestCase
from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.tests.mixins import DataTypesTestCase

__author__ = 'Dominic Dumrauf'


class AlphaTest(DataTypesTestCase, TestCase):
    def setUp(self):
        self.a = Alpha(length=8)

    def test_valid_alpha(self):
        self.assertTrue(self.a.is_valid('        '))
        self.assertTrue(self.a.is_valid('VALID   '))
        self.assertTrue(self.a.is_valid('VALIDTOO'))

    def test_invalid_alpha_wrong_base_set(self):
        self.assertFalse(self.a.is_valid('invalid '))
        self.assertFalse(self.a.is_valid('invalid1'))
        self.assertFalse(self.a.is_valid('VALID0  '))
        self.assertFalse(self.a.is_valid('01234567'))

    def test_invalid_alpha_wrong_justification(self):
        self.assertFalse(self.a.is_valid('   VALID'))

    def test_invalid_alpha_wrong_length(self):
        self._test_invalid_length(valid_length=self.a.length,
                                  valid_char=' ',
                                  data_type=self.a)
