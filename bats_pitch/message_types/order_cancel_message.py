from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.base_36_numeric import Base36Numeric
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types.basic_field import Field
from bats_pitch.message_types.basic_message_type import BasicMessageType

__author__ = 'Dominic Dumrauf'


class OrderCancelMessage(BasicMessageType):
    name = 'Order Cancel Message'

    timestamp = Field(name='Timestamp',
                      offset=0,
                      length=8,
                      data_type=Numeric(length=8))
    message_type = Field(name='Message Type',
                         offset=8,
                         length=1,
                         data_type=SingleCharacter(character='X'))
    order_id = Field(name='Order ID',
                     offset=9,
                     length=12,
                     data_type=Base36Numeric(length=12))
    cancel_shares = Field(name='Cancel Shares',
                          offset=21,
                          length=6,
                          data_type=Numeric(length=6))
    fields = [timestamp,
              message_type,
              order_id,
              cancel_shares]
