from bats_pitch.data_types.alpha import Alpha
from bats_pitch.data_types.base_36_numeric import Base36Numeric
from bats_pitch.data_types.character import SingleCharacter
from bats_pitch.data_types.numeric import Numeric
from bats_pitch.message_types.basic_field import Field
from bats_pitch.message_types.basic_message_type import BasicMessageType

__author__ = 'Dominic Dumrauf'


class AuctionUpdateMessage(BasicMessageType):
    name = 'Auction Update Message'

    timestamp = Field(name='Timestamp',
                      offset=0,
                      length=8,
                      data_type=Numeric(length=8))
    message_type = Field(name='Message Type',
                         offset=8,
                         length=1,
                         data_type=SingleCharacter(character='I'))
    stock_symbol = Field(name='Stock Symbol',
                         offset=9,
                         length=8,
                         data_type=Alpha(length=8))
    auction_type = Field(name='Auction Type',
                         offset=17,
                         length=1,
                         data_type=Alpha(length=1))
    reference_price = Field(name='Reference Price',
                            offset=18,
                            length=10,
                            data_type=Numeric(length=10))
    buy_shares = Field(name='Buy Shares',
                       offset=28,
                       length=10,
                       data_type=Numeric(length=10))
    sell_shares = Field(name='Sell Shares',
                        offset=38,
                        length=10,
                        data_type=Numeric(length=10))
    indicative_price = Field(name='Indicative Price',
                             offset=48,
                             length=10,
                             data_type=Numeric(length=10))
    auction_only_price = Field(name='Auction Only Price',
                               offset=58,
                               length=10,
                               data_type=Numeric(length=10))
    fields = [timestamp,
              message_type,
              stock_symbol,
              auction_type,
              reference_price,
              buy_shares,
              sell_shares,
              indicative_price,
              auction_only_price]
