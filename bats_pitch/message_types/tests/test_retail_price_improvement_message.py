from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types import RetailPriceImprovementMessage
from bats_pitch.message_types.tests.message_type_test_case import MessageTypeTest

__author__ = 'Dominic Dumrauf'


class RetailPriceImprovementMessageTest(MessageTypeTest):
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
                self.DATA_TYPE: SingleCharacter(character='R'),
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
        ]
        self._test_message_type(RetailPriceImprovementMessage, descriptions)
