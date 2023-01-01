from django import forms
from .models import tasks


class Todo_form(forms.ModelForm):
    class Meta():
        model = tasks
        fields = ['task', 'priority', 'date']
