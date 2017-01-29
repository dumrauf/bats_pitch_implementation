from bats_pitch.data_types.basic_data_type import BasicDataType

__author__ = 'Dominic Dumrauf'


class SingleCharacter(BasicDataType):
    def __init__(self, character):
        super(SingleCharacter, self).__init__(length=1,
                                              payload_base_set=character,
                                              justification=BasicDataType.LEFT_JUSTIFICATION,
                                              padding_base_set=None)
