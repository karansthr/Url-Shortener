from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView, ListView
from django.db.models import F
from django.contrib import messages
from django.http import JsonResponse, Http404
from django.views import View
import simplejson

from . import forms
from . import models
from . import utils
from back_office.mixins import PageTitleMixin, ContextMixin, LoginRequiredMixin


class ShortenerView(View):
    def get(self, request):
        raise Http404

    def post(self, request):
        form = forms.URLForm(request.POST or None)
        if form.is_valid():
            suggestion = form.cleaned_data.get('suggestion')
            instance = form.save(commit=False)
            instance.shortened = utils.encode(suggestion)
            if request.user.is_authenticated:
                instance.user = request.user
            instance.save()
            trimmed_url = str(self.request.get_host()) + '/' + str(
                instance.shortened)
            data = {'trimmed_url': trimmed_url}
            return JsonResponse(data)
        else:
            data = simplejson.dumps(form.errors)
            data = {'message': data}
            return JsonResponse(data)


class RedirectorView(RedirectView):
    def get_redirect_url(self, shortened):
        url = get_object_or_404(models.URL, shortened=shortened)
        url.hits = F('hits') + 1
        url.save()
        return url.link


class URLDeleteView(DeleteView):
    model = models.URL
    success_url = '/profile/'

    def get(self, request, *args, **kwargs):
        raise Http404

    def get_object(self):
        url = get_object_or_404(models.URL, shortened=self.kwargs['shortened'])
        if url.user != self.request.user:
            raise Http404
        return url


class HomeView(ContextMixin, TemplateView):
    context = {
        'form': forms.URLForm(),
        'page_title': 'Shorten URL and Create Doc'
    }
    template_name = 'shortener/landing_page.html'


class ProfileView(PageTitleMixin, LoginRequiredMixin, ListView):
    page_title = 'Profile'
    model = models.URL
    context_object_name = 'links'
    template_name = 'shortener/profile.html'

    def get_queryset(self):
        return models.URL.objects.filter(
            user=self.request.user).order_by('-timestamp')
