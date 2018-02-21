from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        exclude = ['timestamp']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            "name": "title"})
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            "name": "subject"})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            "name": "email"})
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            "name": "message"})
