import re

__author__ = 'Dominic Dumrauf'


class BasicDataType(object):
    LEFT_JUSTIFICATION = 'LEFT_JUSTIFICATION'
    RIGHT_JUSTIFICATION = 'RIGHT_JUSTIFICATION'
    JUSTIFICATIONS = [LEFT_JUSTIFICATION,
                      RIGHT_JUSTIFICATION]

    def __init__(self, length, payload_base_set, justification, padding_base_set):
        # Python 2 glitch which allows comparison between empty lists and numbers
        try:
            length - 1
        except TypeError:
            raise AssertionError('The length of a data type needs to be a number.')
        assert length > 0, 'The length of a data type needs to be greater than zero.'
        assert payload_base_set and payload_base_set not in [0, ' '], ('The base set of a data type '
                                                                       'needs to be non-empty.')
        assert justification in self.JUSTIFICATIONS, ('Unknown justification {0}. '
                                                      'Available justifications are {1}'.format(justification,
                                                                                                self.JUSTIFICATIONS))
        self.length = length
        self.payload_base_set = payload_base_set
        self.justification = justification
        self.padding_base_set = padding_base_set
        if self.padding_base_set:
            if self.justification == self.LEFT_JUSTIFICATION:
                self.pattern = r'^{0}*{1}*$'.format(self.payload_base_set,
                                                    self.padding_base_set)
            else:
                self.pattern = r'^{0}*{1}*$'.format(self.padding_base_set,
                                                    self.payload_base_set)
        else:
            self.pattern = r'^{0}{{1}}'.format(self.payload_base_set, self.length)
        self.validator_re = re.compile(self.pattern)

    def is_valid(self, s):
        if not len(s) == self.length:
            return False
        return re.match(self.validator_re, s)

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        return self.length == other.length and \
               self.payload_base_set == other.payload_base_set and \
               self.justification == other.justification and \
               self.padding_base_set == other.padding_base_set
