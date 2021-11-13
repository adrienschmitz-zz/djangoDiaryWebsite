from django import forms
from .models import Day


class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('leave_text', 'gratitude_text',)
