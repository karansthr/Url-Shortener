from django.urls import path, re_path

from . import views

app_name = "shortener"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name="profile"),

    path('shorten', views.ShortenerView.as_view(), name="shortener"),
    re_path(
        r'^(?P<shortened>[\w]+)/$',
        views.RedirectorView.as_view(),
        name="redirector"),
    re_path(
        r'^(?P<shortened>[\w]+)/delete$',
        views.URLDeleteView.as_view(),
        name="url_delete"),
]
