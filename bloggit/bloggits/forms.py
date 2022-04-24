from django import forms

from .models import Bloggit

class BloggitForm(forms.ModelForm):
    class Meta:
        model = Bloggit
        fields = ['text']
        labels = {'text': ''}
        