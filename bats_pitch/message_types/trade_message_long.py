from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.base_36_numeric import Base36Numeric
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types.basic_field import Field
from bats_pitch.message_types.basic_message_type import BasicMessageType

__author__ = 'Dominic Dumrauf'


class TradeMessageLong(BasicMessageType):
    name = 'Trade Message Long'

    timestamp = Field(name='Timestamp',
                      offset=0,
                      length=8,
                      data_type=Numeric(length=8))
    message_type = Field(name='Message Type',
                         offset=8,
                         length=1,
                         data_type=SingleCharacter(character='r'))
    order_id = Field(name='Order ID',
                     offset=9,
                     length=12,
                     data_type=Base36Numeric(length=12))
    side_indicator = Field(name='Side Indicator',
                           offset=21,
                           length=1,
                           data_type=Alpha(length=1))
    shares = Field(name='Shares',
                   offset=22,
                   length=6,
                   data_type=Numeric(length=6))
    stock_symbol = Field(name='Stock Symbol',
                         offset=28,
                         length=8,
                         data_type=Alpha(length=8))
    price = Field(name='Price',
                  offset=36,
                  length=10,
                  data_type=Numeric(length=10))
    execution_id = Field(name='Execution ID',
                         offset=46,
                         length=12,
                         data_type=Base36Numeric(length=12))
    fields = [timestamp,
              message_type,
              order_id,
              side_indicator,
              shares,
              stock_symbol,
              price,
              execution_id]
