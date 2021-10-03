from django import forms
from django.forms import TextInput, Textarea
from home.models import *


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    productid = forms.IntegerField()

class ExportForm(forms.Form):
    date = forms.DateField()
    date1 = forms.DateField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']