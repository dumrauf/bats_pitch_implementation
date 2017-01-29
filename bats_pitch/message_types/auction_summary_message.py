from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types.basic_field import Field
from bats_pitch.message_types.basic_message_type import BasicMessageType

__author__ = 'Dominic Dumrauf'


class AuctionSummaryMessage(BasicMessageType):
    name = 'Auction Summary Message'

    timestamp = Field(name='Timestamp',
                      offset=0,
                      length=8,
                      data_type=Numeric(length=8))
    message_type = Field(name='Message Type',
                         offset=8,
                         length=1,
                         data_type=SingleCharacter(character='J'))
    stock_symbol = Field(name='Stock Symbol',
                         offset=9,
                         length=8,
                         data_type=Alpha(length=8))
    auction_type = Field(name='Auction Type',
                         offset=17,
                         length=1,
                         data_type=Alpha(length=1))
    price = Field(name='Price',
                  offset=18,
                  length=10,
                  data_type=Numeric(length=10))
    shares = Field(name='Shares',
                   offset=28,
                   length=10,
                   data_type=Numeric(length=10))
    fields = [timestamp,
              message_type,
              stock_symbol,
              auction_type,
              price,
              shares]
