from django.db import models
from django.conf import settings
from django.urls import reverse


class URL(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    shortened = models.CharField(max_length=20, default='', primary_key=True)
    hits = models.IntegerField(default=0, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link

    def get_absolute_url(self):
        return reverse('shortener:redirector', kwargs={"url": self.shortened})
