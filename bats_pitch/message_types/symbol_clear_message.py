from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types.basic_field import Field
from bats_pitch.message_types.basic_message_type import BasicMessageType

__author__ = 'Dominic Dumrauf'


class SymbolClearMessage(BasicMessageType):
    name = 'Symbol Clear Message'

    timestamp = Field(name='Timestamp',
                      offset=0,
                      length=8,
                      data_type=Numeric(length=8))
    message_type = Field(name='Message Type',
                         offset=8,
                         length=1,
                         data_type=SingleCharacter(character='s'))
    stock_symbol = Field(name='Stock Symbol',
                         offset=9,
                         length=8,
                         data_type=Alpha(length=8))
    fields = [timestamp,
              message_type,
              stock_symbol]
