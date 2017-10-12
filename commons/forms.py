from django import forms

from commons.config.datatype import DataType


class DataSpecForm(forms.Form):
    data_length = forms.IntegerField(label="Number of records to generate",
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))
    field_length = forms.IntegerField(label="Number of fields per record",
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))


class FieldSpecForm(forms.Form):
    data_type = forms.ChoiceField([(name, name) for name, member in DataType.__members__.items()],
                                  widget=forms.Select(attrs={'class': 'regDropDown'}))
    field_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
