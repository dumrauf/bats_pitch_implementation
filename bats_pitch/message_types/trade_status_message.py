from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.base_36_numeric import Base36Numeric
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types.basic_field import Field
from bats_pitch.message_types.basic_message_type import BasicMessageType

__author__ = 'Dominic Dumrauf'


class TradeStatusMessage(BasicMessageType):
    name = 'Trade Status Message'

    timestamp = Field(name='Timestamp',
                      offset=0,
                      length=8,
                      data_type=Numeric(length=8))
    message_type = Field(name='Message Type',
                         offset=8,
                         length=1,
                         data_type=SingleCharacter(character='H'))
    stock_symbol = Field(name='Stock Symbol',
                         offset=9,
                         length=8,
                         data_type=Alpha(length=8))
    halt_status = Field(name='Halt Status',
                        offset=17,
                        length=1,
                        data_type=Alpha(length=1))
    reg_sho_action = Field(name='Reg SHO Action',
                           offset=18,
                           length=1,
                           data_type=Numeric(length=1))
    reserved_1 = Field(name='Reserved1',
                       offset=19,
                       length=1,
                       data_type=Alpha(length=1))
    reserved_2 = Field(name='Reserved2',
                       offset=20,
                       length=1,
                       data_type=Alpha(length=1))
    fields = [timestamp,
              message_type,
              stock_symbol,
              halt_status,
              reg_sho_action,
              reserved_1,
              reserved_2]
