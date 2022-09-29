from django import forms
from django.forms import widgets

from todo_app.models import TaskStatus


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    detailed_description = forms.CharField(max_length=3000, required=False, label='Detailed Description',
                                           widget=widgets.Textarea)
    deadline = forms.DateField(required=False, label='Due Date')
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all())
