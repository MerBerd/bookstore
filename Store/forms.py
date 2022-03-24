from attr import field
from django import forms
from django.forms import widgets

from .models import Book, Author

class NewAuthorForm(forms.ModelForm):
    pass

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Description', 'Price', 'Photo', 'Author']
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Description':widgets.Textarea(attrs={'cols' : 60, 'rows' : 10, 'class' : 'form-control'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control'}),
            'Photo': forms.URLInput(attrs={'class': 'form-control'}),
            'Author': widgets.SelectMultiple()
        }

class NewAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['FirstName', 'LastName', 'Patronymic']
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Patronymic': forms.TextInput(attrs={'class': 'form-control'}),
        }

