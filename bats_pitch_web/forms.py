from django.forms import Form, FileField

__author__ = 'Dominic Dumrauf'


class BATSPitchFileForm(Form):
    file = FileField(label='',
                     help_text='')
