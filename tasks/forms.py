from django import forms
from . import models

class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ('status', 'title', 'description', 'related_deliv')
