from unittest import TestCase

__author__ = 'Dominic Dumrauf'


class MessageTypeTest(TestCase):
    OFFSET = 'OFFSET'
    LENGTH = 'LENGTH'
    DATA_TYPE = 'DATA_TYPE'

    def setUp(self):
        self.is_verbose = False

    def _test_message_type(self, message_type, descriptions):
        for description, field in zip(descriptions, message_type.fields):
            if self.is_verbose:
                print 'Checking field {0} of message type {1}'.format(field.name,
                                                                      message_type.name)
            self.assertEqual(description[self.OFFSET], field.offset)
            self.assertEqual(description[self.LENGTH], field.length)
            self.assertEqual(description[self.DATA_TYPE], field.data_type)
