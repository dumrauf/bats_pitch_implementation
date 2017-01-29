from bats_pitch.message_types.add_order_message_long import AddOrderMessageLong
from bats_pitch.message_types.add_order_message import AddOrderMessage
from bats_pitch.message_types.auction_summary_message import AuctionSummaryMessage
from bats_pitch.message_types.auction_update_message import AuctionUpdateMessage
from bats_pitch.message_types.order_cancel_message import OrderCancelMessage
from bats_pitch.message_types.order_executed_message import OrderExecutedMessage
from bats_pitch.message_types.retail_price_improvement_message import RetailPriceImprovementMessage
from bats_pitch.message_types.symbol_clear_message import SymbolClearMessage
from bats_pitch.message_types.trade_break_message import TradeBreakMessage
from bats_pitch.message_types.trade_message import TradeMessage
from bats_pitch.message_types.trade_message_long import TradeMessageLong
from bats_pitch.message_types.trade_status_message import TradeStatusMessage

__author__ = 'Dominic Dumrauf'


KNOWN_MESSAGE_TYPES = [
    SymbolClearMessage,
    AddOrderMessage,
    AddOrderMessageLong,
    OrderExecutedMessage,
    OrderCancelMessage,
    TradeMessage,
    TradeMessageLong,
    TradeBreakMessage,
    TradeStatusMessage,
    AuctionUpdateMessage,
    AuctionSummaryMessage,
    RetailPriceImprovementMessage,
]
