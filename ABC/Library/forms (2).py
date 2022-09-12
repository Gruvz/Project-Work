from .models import Books
from django import forms
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class Addbook_form(forms.ModelForm):

    class Meta:
        model = Books
        fields = ['Title', 'Create', 'Author']


    # widgets = {
    #     'Create': forms.Select(attrs={'class': 'tmp-form'})
    # }

    Create = forms.ModelChoiceField(
         queryset=User.objects.all(),
         initial=User.objects.first(),
         label='Кто добавил:',
         widget=forms.Select(attrs={'class': 'tmp-form'})
    )


    Title = forms.CharField(label='Название', max_length=255,
                            widget=forms.TextInput(attrs={'class': 'tmp-form', 'placeholder': 'Название'}))

    Author = forms.CharField(label='Автор', max_length=255,
                            widget=forms.TextInput(attrs={'class': 'tmp-form', 'placeholder': 'Автор произведения'}))


