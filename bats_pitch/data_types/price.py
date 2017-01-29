from bats_pitch.data_types.basic_data_type import BasicDataType

__author__ = 'Dominic Dumrauf'


class WholeNumberDigits(BasicDataType):
    def __init__(self):
        super(WholeNumberDigits, self).__init__(length=6,
                                                payload_base_set='[0-9]',
                                                justification=BasicDataType.RIGHT_JUSTIFICATION,
                                                padding_base_set='0')


class DecimalDigitsNumber(BasicDataType):
    def __init__(self):
        super(DecimalDigitsNumber, self).__init__(length=4,
                                                  payload_base_set='[0-9]',
                                                  justification=BasicDataType.LEFT_JUSTIFICATION,
                                                  padding_base_set='0')


class Price(object):
    def __init__(self):
        self.length = 10
        self.whole_number_digits = WholeNumberDigits()
        self.decimal_digits_number = DecimalDigitsNumber()

    def is_valid(self, s):
        return len(s) == 10 and \
               self.whole_number_digits.is_valid(s[:6]) and \
               self.decimal_digits_number.is_valid(s[6:10])
