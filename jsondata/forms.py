from django import forms

from jsondata.config.datatype import DataType


class DataSpecForm(forms.Form):
    data_length = forms.IntegerField(label="Number of records to generate")
    field_length = forms.IntegerField(label="Number of fields per record")


class FieldSpecForm(forms.Form):
    data_type = forms.ChoiceField([(name, name) for name, member in DataType.__members__.items()],
                                  widget=forms.Select(attrs={'class': 'regDropDown'}))
    field_name = forms.CharField()
