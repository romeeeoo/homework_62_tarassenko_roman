from django import forms
from django.contrib.auth.models import User

from todo_app.models import TaskStatus, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), initial=TaskStatus.objects.first())

        model = Task
        fields = ["summary",
                  "description",
                  "status",
                  "types", ]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "specification",
            "start_date",
            "project_deadline",
        ]


class ProjectTaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), initial=TaskStatus.objects.filter(name="new"))

    class Meta:
        model = Task
        fields = [
            "summary",
            "description",
            "status",
            "types",
        ]


# class AddUserToProjectForm(forms.ModelForm):
#     username = forms.ModelChoiceField(queryset=User.objects.all())
#
#     class Meta:
#         model = User
#         fields = ["username"]

class AddUserToProjectForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())

