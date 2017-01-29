from unittest import TestCase
from bats_pitch.message_types import AddOrderMessage, TradeMessage, OrderCancelMessage, OrderExecutedMessage
from bats_pitch.message_types.validator import get_message_type

__author__ = 'Dominic Dumrauf'


class ValidatorTest(TestCase):
    def test_get_message_type_add_order_message(self):
        self.assertEqual(AddOrderMessage, get_message_type('28800011AAK27GA0000DTS000100SH    0000619200Y'))

    def test_get_message_type_order_executed_message(self):
        self.assertEqual(OrderExecutedMessage, get_message_type('28803224E4K27GA00003G00007700004AQ00001'))

    def test_get_message_type_order_cancel_message(self):
        self.assertEqual(OrderCancelMessage, get_message_type('28800168X1K27GA00000Y000100'))

    def test_get_message_type_trade_message(self):
        self.assertEqual(TradeMessage, get_message_type('28803240P4K27GA00003PB000100DXD   0000499600000N4AQ00003'))

    def test_get_message_type_for_all_remaining_messages(self):
        """
        This placeholder test needs to be implemented testing the functionality that the name suggests.
        """
        pass

    def test_get_message_no_matching_message_type(self):
        self.assertIsNone(get_message_type('THIS SH0ULD NOT MATCH ANY MESSAGE TYPE'))
