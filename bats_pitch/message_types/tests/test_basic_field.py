from unittest import TestCase
from bats_pitch.message_types.basic_field import Field

__author__ = 'Dominic Dumrauf'


class O(object):
    """
    Synthetic object to circumvent the problem of assigning
    attributes to native objects.
    """
    pass


class BasicFieldTest(TestCase):
    def test_length_mismatch(self):
        obj = O()
        obj.length = 2
        self.assertRaises(AssertionError, Field,
                          name='Irrelevant',
                          offset=0,
                          length=1,
                          data_type=obj)

    def test_matching_length(self):
        obj = O()
        obj.length = 1
        Field(name='Irrelevant',
              offset=0,
              length=1,
              data_type=obj)

    def test_is_valid_with_valid_fields(self):
        """
        This placeholder test needs to be implemented testing the functionality that the name suggests.
        """
        pass

    def test_is_valid_with_invalid_fields(self):
        """
        This placeholder test needs to be implemented testing the functionality that the name suggests.
        """
        pass
