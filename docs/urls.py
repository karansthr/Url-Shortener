from django.urls import path, re_path

from . import views

app_name = "docs"

urlpatterns = [
    path('', views.DocCreateView.as_view(), name="post_create"),
    re_path(
        r'^(?P<url>[\w]+)/$', views.DocDetailView.as_view(),
        name="doc_detail"),
    re_path(
        r'^(?P<url>[\w]+)/edit$',
        views.DocUpdateView.as_view(),
        name="doc_update"),
    re_path(
        r'^(?P<url>[\w]+)/delete', views.DocDeleteView, name="doc_delete"),
]
