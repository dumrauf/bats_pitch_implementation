from bats_pitch.data_types.basic_data_type import BasicDataType

__author__ = 'Dominic Dumrauf'


class Alpha(BasicDataType):
    def __init__(self, length):
        super(Alpha, self).__init__(length=length,
                                    payload_base_set='[A-Z]',
                                    justification=BasicDataType.LEFT_JUSTIFICATION,
                                    padding_base_set=' ')
