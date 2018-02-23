from django.urls import re_path

from .views import UrlCreateAPIView

app_name = 'shortener'

urlpatterns = [
    re_path(
        r'^create/', UrlCreateAPIView.as_view(), name="api_create")
]
