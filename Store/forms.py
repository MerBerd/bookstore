from django import forms
from django.forms import widgets

from .models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Description', 'Price', 'Photo', 'Author']
        widgets = {
            'Description':widgets.Textarea(attrs={'cols' : 80, 'rows' : 20, 'class' : 'form-control'}),
        }