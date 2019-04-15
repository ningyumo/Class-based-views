from django import forms
from .models import Author


class BlogForm(forms.Form):
    author = Author.objects.values_list('pk', 'name')
    author_choices = tuple(author)

    title = forms.CharField(max_length=30, label="title")
    text = forms.CharField(label="text", widget=forms.TextInput)
    author = forms.ChoiceField(label="author", choices=author_choices)

