from bats_pitch.data_types.basic_data_type import BasicDataType

__author__ = 'Dominic Dumrauf'


class Timestamp(BasicDataType):
    def __init__(self, length):
        super(Timestamp, self).__init__(length=length,
                                        payload_base_set='[0-9]',
                                        justification=BasicDataType.RIGHT_JUSTIFICATION,
                                        padding_base_set='0')
