from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate

from back_office.mixins import PageTitleMixin
from . import forms


class LoginView(FormView, PageTitleMixin):
    form_class = forms.LoginForm
    success_url = '/profile'
    page_title = 'Login'
    template_name = 'accounts/login_form.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class RegisterView(CreateView, PageTitleMixin):
    form_class = forms.RegistrationForm
    success_url = '/login'
    template_name = 'accounts/registration_form.html'
    page_title = 'Registration'
