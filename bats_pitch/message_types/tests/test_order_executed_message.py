from bats_pitch.data_types.base_36_numeric import Base36Numeric
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types import OrderExecutedMessage
from bats_pitch.message_types.tests.message_type_test_case import MessageTypeTest

__author__ = 'Dominic Dumrauf'


class OrderExecutedMessageTest(MessageTypeTest):
    def test_message(self):
        descriptions = [
            {
                self.OFFSET: 0,
                self.LENGTH: 8,
                self.DATA_TYPE: Numeric(length=8),
            },
            {
                self.OFFSET: 8,
                self.LENGTH: 1,
                self.DATA_TYPE: SingleCharacter(character='E'),
            },
            {
                self.OFFSET: 9,
                self.LENGTH: 12,
                self.DATA_TYPE: Base36Numeric(length=12),
            },
            {
                self.OFFSET: 21,
                self.LENGTH: 6,
                self.DATA_TYPE: Numeric(length=6),
            },
            {
                self.OFFSET: 27,
                self.LENGTH: 12,
                self.DATA_TYPE: Base36Numeric(length=12),
            },
        ]
        self._test_message_type(OrderExecutedMessage, descriptions)
