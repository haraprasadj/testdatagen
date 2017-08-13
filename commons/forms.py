from django import forms

from commons.config.datatype import DataType


class DataSpecForm(forms.Form):
    data_length = forms.IntegerField(label="Number of records to generate", max_value=50)
    field_length = forms.IntegerField(label="Number of fields per record", max_value=5)


class FieldSpecForm(forms.Form):
    data_type = forms.ChoiceField([(name, name) for name, member in DataType.__members__.items()],
                                  widget=forms.Select(attrs={'class': 'regDropDown'}))
    field_name = forms.CharField()