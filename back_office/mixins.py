from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.http import Http404


class PageTitleMixin:
    page_title = ""

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        return context


class ContextMixin:
    context = {}

    def get_context(self):
        return self.context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {**context, **self.get_context()}
        return context


class LoginRequiredMixin(LRM):
    def handle_no_permission(self):
        raise Http404
