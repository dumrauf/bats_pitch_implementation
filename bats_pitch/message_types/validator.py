from bats_pitch.message_types import KNOWN_MESSAGE_TYPES

__author__ = 'Dominic Dumrauf'


def get_message_type(s):
    for known_message_type in KNOWN_MESSAGE_TYPES:
        if known_message_type.is_valid(s):
            return known_message_type
    return None
