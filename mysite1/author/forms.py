from django import forms
from .models import Author #, Book


class AuthorForm (forms.ModelForm):
    class Meta:
        model = Author
        fields= ['full_name' , 'email' ]





