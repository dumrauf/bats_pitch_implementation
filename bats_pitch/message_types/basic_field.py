__author__ = 'Dominic Dumrauf'


class Field(object):
    def __init__(self, name, offset, length, data_type):
        assert length == data_type.length, 'The length of the field and the length of the data type need to match.'
        self.name = name
        self.offset = offset
        self.length = length
        self.data_type = data_type

    def is_valid(self, s):
        return self.data_type.is_valid(s)
