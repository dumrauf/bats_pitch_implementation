from collections import OrderedDict
from bats_pitch.message_types import KNOWN_MESSAGE_TYPES
from bats_pitch.message_types.validator import get_message_type

__author__ = 'Dominic Dumrauf'

UNRECOGNIZED_LINES = 'Unrecognized Lines'
TOTAL_MESSAGES = 'Number of Lines'


def _get_line(l):
    """
    Removes a leading 'S' if present in the given line 'l'.
    """
    if l.startswith('S'):
        return l[1:]
    else:
        return l

def _get_new_analysis_dict():
    """
    Returns a dictionary which contains all known messages and an initial count
    of zero messages for each type.
    """
    detected_messages = OrderedDict()
    for known_message_type in KNOWN_MESSAGE_TYPES:
        detected_messages[known_message_type.name] = 0
    detected_messages[UNRECOGNIZED_LINES] = 0
    detected_messages[TOTAL_MESSAGES] = 0
    return detected_messages


def analyze_stream(stream):
    """
    Analyzes a given 'stream' and creates a statistic about the number of message
    types in the stream.
    """
    detected_messages = _get_new_analysis_dict()
    analysis = []
    for line_nr, raw_line in enumerate(stream):
        clean_line = _get_line(raw_line)
        detected_messages_type = get_message_type(clean_line)
        if detected_messages_type:
            detected_messages[detected_messages_type.name] += 1
        else:
            detected_messages[UNRECOGNIZED_LINES] += 1
        detected_messages[TOTAL_MESSAGES] += 1
        analysis.append({
            'line_nr': line_nr,
            'raw_line': raw_line,
            'clean_line': clean_line,
            'detected_messages_type': detected_messages_type,
        })
    return detected_messages, analysis
