from django import forms
from .models import Salary, Worklog, Travelex





class WorklogModelForm(forms.ModelForm):
    class Meta:
        model = Worklog
        fields = ['date', 'file', 'comment']

        widgets = {
            'date': forms.TextInput(attrs={'class': 'vDateField'})
        }




class TravelexModelForm(forms.ModelForm):
    class Meta:
        model = Travelex
        fields = ['start_place', 'end_place', 'date', 'value', 'reason']

        widgets = {
            'date': forms.TextInput(attrs={'class': 'vDateField'})
        }