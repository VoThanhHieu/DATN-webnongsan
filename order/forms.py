from django import forms

class DateInput(forms.DateInput):
    input_type = 'month'

class DateForm(forms.Form):
    my_date = forms.DateField(widget=DateInput)

class DateModelForm(forms.Form):
    class Meta:
        widgets = {'my_date': DateInput()}