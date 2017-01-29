from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types import TradeStatusMessage
from bats_pitch.message_types.tests.message_type_test_case import MessageTypeTest

__author__ = 'Dominic Dumrauf'


class TradeStatusMessageTest(MessageTypeTest):
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
                self.DATA_TYPE: SingleCharacter(character='H'),
            },
            {
                self.OFFSET: 9,
                self.LENGTH: 8,
                self.DATA_TYPE: Alpha(length=8),
            },
            {
                self.OFFSET: 17,
                self.LENGTH: 1,
                self.DATA_TYPE: Alpha(length=1),
            },
            {
                self.OFFSET: 18,
                self.LENGTH: 1,
                self.DATA_TYPE: Numeric(length=1),
            },
            {
                self.OFFSET: 19,
                self.LENGTH: 1,
                self.DATA_TYPE: Alpha(length=1),
            },
            {
                self.OFFSET: 20,
                self.LENGTH: 1,
                self.DATA_TYPE: Alpha(length=1),
            },
        ]
        self._test_message_type(TradeStatusMessage, descriptions)
