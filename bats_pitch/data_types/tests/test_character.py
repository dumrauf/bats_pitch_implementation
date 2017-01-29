from unittest import TestCase
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.tests.mixins import DataTypesTestCase

__author__ = 'Dominic Dumrauf'


class CharacterTest(DataTypesTestCase, TestCase):
    def setUp(self):
        self.c = SingleCharacter(character='C')

    def test_valid_character(self):
        self.assertTrue(self.c.is_valid('C'))

    def test_invalid_character_wrong_base_set(self):
        self.assertFalse(self.c.is_valid(' '))
        self.assertFalse(self.c.is_valid('0'))
        self.assertFalse(self.c.is_valid('c'))

    def test_invalid_character_wrong_length(self):
        self._test_invalid_length(valid_length=self.c.length,
                                  valid_char='C',
                                  data_type=self.c)
