import re
from django import forms
from tinymce import TinyMCE
from . import models


class DocForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={
            'cols': 30,
            'rows': 10
        }))
    title = forms.CharField(
        max_length=70,
        label='Title',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '( optional )'
        }))
    suggestion = forms.CharField(
        max_length=10,
        label='Custom short link',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '( optional )'
        }))

    class Meta:
        model = models.Doc
        fields = '__all__'
        exclude = ['url', 'user']

    def clean_suggestion(self):
        suggestion = self.cleaned_data['suggestion']

        if suggestion:
            if suggestion in [
                    'about', 'disclaimer', 'contact', 'sitemap.xml',
                    'robots.txt', 'login', 'register', 'sitemap', 'doc',
                    'admin', 'karan', 'resume', 'profile', 'logout'
            ]:
                raise forms.ValidationError(
                    'Please choose another custom short link, ' + suggestion +
                    ' is reserverd.')

            if not re.match("^[A-Za-z0-9_-]*$", suggestion):
                raise forms.ValidationError(
                    " It should contain only alpha-numeric and/or _ ")

            if models.URL.objects.filter(shortened=suggestion).exists():
                raise forms.ValidationError("Please choose another, '" +
                                            suggestion + "' already exists.")

        return suggestion
