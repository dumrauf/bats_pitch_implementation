from unittest import TestCase
from bats_pitch.message_types import KNOWN_MESSAGE_TYPES

__author__ = 'Dominic Dumrauf'


class MessageTypesTest(TestCase):
    def setUp(self):
        self.is_verbose = False

    def test_field_length_matches_data_type_field_length(self):
        """
        Tests that for each known message type, the length of each field matches the length of
        the corresponding data type field.
        """
        for known_message_type in KNOWN_MESSAGE_TYPES:
            for field in known_message_type.fields:
                if self.is_verbose:
                    print 'Checking length setup of field {0} in message {1}'.format(field.name, known_message_type.name)
                self.assertEqual(field.length, field.data_type.length)

    def test_message_type_uniqueness(self):
        """
        Test that each message type occurs only once in the list of known message types.
        """
        message_type_characters = map(lambda x: x.message_type.data_type.payload_base_set,
                                      KNOWN_MESSAGE_TYPES)
        for message_type_character in message_type_characters:
            if self.is_verbose:
                print 'Checking uniqueness of message type {0}'.format(message_type_character)
            self.assertEqual(1, len(filter(lambda x : x == message_type_character, message_type_characters)))

    def test_message_type_fields_succinctness(self):
        """
        Tests that for each message type, the offsets and lengths of fields are non-overlapping and succinct.
        """
        for known_message_type in KNOWN_MESSAGE_TYPES:
            current_index = 0
            for field in known_message_type.fields:
                if self.is_verbose:
                    print 'Checking offset of field {0} in message {1}'.format(field.name, known_message_type.name)
                self.assertEqual(current_index, field.offset)
                current_index += field.length

    def test_message_type_name_uniqueness(self):
        """
        Tests that each known message type has a unique name.
        """
        message_type_names = map(lambda x: x.name, KNOWN_MESSAGE_TYPES)
        for message_type_name in message_type_names:
            if self.is_verbose:
                print 'Checking uniqueness of message type name {0}'.format(message_type_name)
            self.assertEqual(1, len(filter(lambda x: x == message_type_name, message_type_names)))
