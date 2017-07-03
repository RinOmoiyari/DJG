from django import forms
from . import models

class DeliverableForm(forms.ModelForm):

    class Meta:
        model = models.Deliverable
        fields = ('status', 'title', 'request',)
