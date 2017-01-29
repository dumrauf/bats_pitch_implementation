from collections import OrderedDict
import random
import string
from django.test import TestCase
from bats_pitch.message_types import KNOWN_MESSAGE_TYPES, AddOrderMessage
from bats_pitch_web.utils import _get_line, UNRECOGNIZED_LINES, TOTAL_MESSAGES, _get_new_analysis_dict, analyze_stream

__author__ = 'Dominic Dumrauf'


class ViewsTest(TestCase):

    def test_get_line_with_leading_s(self):
        self.assertEqual('', _get_line('S'))
        self.assertEqual('S', _get_line('SS'))
        for i in xrange(100):
            s = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(i))
            self.assertEqual(s, _get_line('S{0}'.format(s)))

    def test_get_line_without_leading_s(self):
        self.assertEqual('', _get_line(''))
        self.assertEqual('TEST', _get_line('TEST'))
        for i in xrange(100):
            s = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(i))
            if not s.startswith('S'):
                self.assertEqual(s, _get_line(s))

    def test_get_new_analysis_dict(self):
        d = OrderedDict()
        for known_message_type in KNOWN_MESSAGE_TYPES:
            d[known_message_type.name] = 0
        d[UNRECOGNIZED_LINES] = 0
        d[TOTAL_MESSAGES] = 0
        self.assertEqual(d, _get_new_analysis_dict())

    def test_analyze_stream_add_order_message(self):
        stream = ['28800011AAK27GA0000DTS000100SH    0000619200Y',
                  '28800012ABK27GA00000KB001000SSO   0000763800Y']
        detected_messages, analysis = analyze_stream(stream)
        self.assertEqual(2, detected_messages[AddOrderMessage.name])
        self.assertEqual(2, detected_messages[TOTAL_MESSAGES])
        self.assertEqual(0, detected_messages[UNRECOGNIZED_LINES])
        self.assertEqual(analysis, [
            {
                'line_nr': 0,
                'raw_line': stream[0],
                'clean_line': stream[0],
                'detected_messages_type': AddOrderMessage,
            },
            {
                'line_nr': 1,
                'raw_line': stream[1],
                'clean_line': stream[1],
                'detected_messages_type': AddOrderMessage,
            },
        ])

    def test_analyze_stream_all_remaining_message_types(self):
        """
        This test is a placeholder test for the remaining tests for all message types
        in the BATS pitch protocol.
        """
        pass
