from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from . import forms
from .mixins import PageTitleMixin


class AboutView(PageTitleMixin, TemplateView):
    page_title = 'About'
    template_name = 'back_office/about.html'


class ContactView(PageTitleMixin, CreateView):
    page_title = 'Contact'
    form_class = forms.ContactForm
    template_name = 'back_office/contact_form.html'
    success_url = '/'
