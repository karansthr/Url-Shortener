from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
