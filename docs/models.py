from django.db import models
from django.urls import reverse

from tinymce import HTMLField
from shortener.models import URL


class Doc(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = HTMLField('Content')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("docs:doc_detail", kwargs={"url": self.url.shortened})

    def __str__(self):
        return self.title
