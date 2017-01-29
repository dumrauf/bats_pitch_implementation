from bats_pitch.data_types.basic_data_type import BasicDataType

__author__ = 'Dominic Dumrauf'


class Base36Numeric(BasicDataType):
    def __init__(self, length):
        super(Base36Numeric, self).__init__(length=length,
                                            payload_base_set='[0-9A-Z]',
                                            justification=BasicDataType.RIGHT_JUSTIFICATION,
                                            padding_base_set='0')
