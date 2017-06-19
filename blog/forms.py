from django import forms
from . import models

class PostForm(forms.ModelForm):

    class Meta:
        model = models.BlogPost
        fields = ('title', 'body',)
