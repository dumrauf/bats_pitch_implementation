from unittest import TestCase
from bats_pitch.data_types.basic_data_type import BasicDataType

__author__ = 'Dominic Dumrauf'


class TestBasicDataType(TestCase):
    def setUp(self):
        self.valid_length = 8
        self.valid_payload_base_set = '[0-9]'
        self.valid_justification = BasicDataType.RIGHT_JUSTIFICATION
        self.valid_padding_base_set = ' '

    def test_justifications(self):
        self.assertIn(BasicDataType.LEFT_JUSTIFICATION, BasicDataType.JUSTIFICATIONS)
        self.assertIn(BasicDataType.RIGHT_JUSTIFICATION, BasicDataType.JUSTIFICATIONS)

    def test_empty_length(self):
        for empty in [0, None, [], (), '']:
            self.assertRaises(AssertionError,
                              BasicDataType,
                              empty,
                              self.valid_payload_base_set,
                              self.valid_justification,
                              self.valid_padding_base_set)

    def test_empty_payload_base(self):
        for empty in [None, [], (), '']:
            self.assertRaises(AssertionError,
                              BasicDataType,
                              self.valid_length,
                              empty,
                              self.valid_justification,
                              self.valid_padding_base_set)

    def test_wrong_justification(self):
        self.assertRaises(AssertionError,
                          BasicDataType,
                          self.valid_length,
                          self.valid_payload_base_set,
                          'UNKNOWN_JUSTIFICATION',
                          self.valid_padding_base_set)

    def test_correct_basic_data_type(self):
        BasicDataType(length=self.valid_length,
                      payload_base_set=self.valid_payload_base_set,
                      justification=self.valid_justification,
                      padding_base_set=self.valid_padding_base_set)

    def test_equality(self):
        a = BasicDataType(length=self.valid_length,
                          payload_base_set=self.valid_payload_base_set,
                          justification=self.valid_justification,
                          padding_base_set=self.valid_padding_base_set)
        b = BasicDataType(length=self.valid_length,
                          payload_base_set=self.valid_payload_base_set,
                          justification=self.valid_justification,
                          padding_base_set=self.valid_padding_base_set)
        self.assertFalse(a != b)
        self.assertTrue(a == b)

    def test_inequality_in_length(self):
        a = BasicDataType(length=1,
                          payload_base_set=self.valid_payload_base_set,
                          justification=self.valid_justification,
                          padding_base_set=self.valid_padding_base_set)
        b = BasicDataType(length=2,
                          payload_base_set=self.valid_payload_base_set,
                          justification=self.valid_justification,
                          padding_base_set=self.valid_padding_base_set)
        self.assertTrue(a != b)
        self.assertFalse(a == b)

    def test_inequality_in_payload_base_set(self):
        a = BasicDataType(length=self.valid_length,
                          payload_base_set='[A-Z]',
                          justification=self.valid_justification,
                          padding_base_set=self.valid_padding_base_set)
        b = BasicDataType(length=self.valid_length,
                          payload_base_set='[0-9]',
                          justification=self.valid_justification,
                          padding_base_set=self.valid_padding_base_set)
        self.assertTrue(a != b)
        self.assertFalse(a == b)

    def test_inequality_in_justification(self):
        a = BasicDataType(length=self.valid_length,
                          payload_base_set=self.valid_payload_base_set,
                          justification=BasicDataType.LEFT_JUSTIFICATION,
                          padding_base_set=self.valid_padding_base_set)
        b = BasicDataType(length=self.valid_length,
                          payload_base_set=self.valid_payload_base_set,
                          justification=BasicDataType.RIGHT_JUSTIFICATION,
                          padding_base_set=self.valid_padding_base_set)
        self.assertTrue(a != b)
        self.assertFalse(a == b)

    def test_inequality_in_padding_base_set(self):
        a = BasicDataType(length=self.valid_length,
                          payload_base_set=self.valid_payload_base_set,
                          justification=self.valid_justification,
                          padding_base_set='[A-Z]')
        b = BasicDataType(length=self.valid_length,
                          payload_base_set=self.valid_payload_base_set,
                          justification=self.valid_justification,
                          padding_base_set='[0-9]')
        self.assertTrue(a != b)
        self.assertFalse(a == b)


class TestBasicRightJustifiedDataType(TestCase):
    def setUp(self):
        self.b = BasicDataType(length=8,
                               payload_base_set='[0-9]',
                               justification=BasicDataType.RIGHT_JUSTIFICATION,
                               padding_base_set=' ')

    def test_valid_input(self):
        self.assertTrue(self.b.is_valid('        '))
        self.assertTrue(self.b.is_valid('       1'))
        self.assertTrue(self.b.is_valid('01234567'))

    def test_invalid_input_wrong_length(self):
        for i in xrange(self.b.length):
            self.assertFalse(self.b.is_valid(' ' * i))

    def test_invalid_input_wrong_base_set(self):
        self.assertFalse(self.b.is_valid('       i'))
        self.assertFalse(self.b.is_valid('       I'))
        self.assertFalse(self.b.is_valid('   VALID'))
        self.assertFalse(self.b.is_valid('notvalid'))
        self.assertFalse(self.b.is_valid('NOTVALID'))

    def test_invalid_justification(self):
        self.assertFalse(self.b.is_valid('0       '))
        self.assertFalse(self.b.is_valid('0123456 '))



class TestBasicLeftJustifiedDataType(TestCase):
    def setUp(self):
        self.b = BasicDataType(length=8,
                               payload_base_set='[0-9]',
                               justification=BasicDataType.LEFT_JUSTIFICATION,
                               padding_base_set=' ')

    def test_valid_input(self):
        self.assertTrue(self.b.is_valid('        '))
        self.assertTrue(self.b.is_valid('1       '))
        self.assertTrue(self.b.is_valid('01234567'))

    def test_invalid_input_wrong_length(self):
        for i in xrange(self.b.length):
            self.assertFalse(self.b.is_valid(' ' * i))

    def test_invalid_input_wrong_base_set(self):
        self.assertFalse(self.b.is_valid('i       '))
        self.assertFalse(self.b.is_valid('I       '))
        self.assertFalse(self.b.is_valid('VALID   '))
        self.assertFalse(self.b.is_valid('notvalid'))
        self.assertFalse(self.b.is_valid('NOTVALID'))

    def test_invalid_justification(self):
        self.assertFalse(self.b.is_valid('       0'))
        self.assertFalse(self.b.is_valid(' 0123456'))
