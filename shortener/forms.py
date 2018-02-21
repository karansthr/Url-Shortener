from django import forms
from .models import URL
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import re

val = URLValidator()


class URLForm(forms.ModelForm):

    link = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Paste a link to shorten'
        }))
    suggestion = forms.CharField(
        min_length=3,
        max_length=10,
        label='Custom link suggestion',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '( optional )'
        }))

    class Meta:
        model = URL
        fields = '__all__'
        exclude = ['shortened', 'user', 'hits']

    def clean_link(self):
        link = self.cleaned_data.get('link')
        if link is None:
            raise forms.ValidationError("Please enter a valid URL")

        link = 'http://' + link if link[:4] != 'http' else link

        try:
            val(link)
        except ValidationError as e:
            raise forms.ValidationError("Please enter a valid URL")

        return link

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

            if URL.objects.filter(shortened=suggestion).exists():
                raise forms.ValidationError("Please choose another, '" +
                                            suggestion + "' already exists.")

        return suggestion
