__author__ = 'Dominic Dumrauf'


class BasicMessageType(object):
    fields = []

    @classmethod
    def is_valid(cls, s):
        is_valid_message_type = True
        for field in cls.fields:
            payload_start = field.offset
            payload_end = field.offset + field.length
            is_valid_message_type = is_valid_message_type and field.is_valid(s[payload_start:payload_end])
            if not is_valid_message_type:
                return False
        return True
