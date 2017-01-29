from unittest import TestCase
from bats_pitch.data_types.price import Price
from bats_pitch.data_types.tests.mixins import DataTypesTestCase

__author__ = 'Dominic Dumrauf'


class NumericTest(DataTypesTestCase, TestCase):
    def setUp(self):
        self.p = Price()

    def test_valid_price(self):
        self.assertTrue(self.p.is_valid('0000000000'))
        self.assertTrue(self.p.is_valid('0000011000'))

    def test_valid_price_whole_number(self):
        self.assertTrue(self.p.is_valid('0000010000'))
        self.assertTrue(self.p.is_valid('1234560000'))

    def test_valid_price_decimal_digits_number(self):
        self.assertTrue(self.p.is_valid('0000001000'))
        self.assertTrue(self.p.is_valid('0000001234'))

    def test_invalid_price_wrong_base_set(self):
        self.assertFalse(self.p.is_valid('          '))
        self.assertFalse(self.p.is_valid(' 123456789'))
        self.assertFalse(self.p.is_valid('00000i0000'))
        self.assertFalse(self.p.is_valid('000000i000'))
        self.assertFalse(self.p.is_valid('00000ii000'))
        self.assertFalse(self.p.is_valid('invalid000'))
        self.assertFalse(self.p.is_valid('invalidtoo'))
        self.assertFalse(self.p.is_valid('INVALIDTOO'))

    def test_invalid_price_wrong_length(self):
        self._test_invalid_length(valid_length=self.p.length,
                                  valid_char='0',
                                  data_type=self.p)
