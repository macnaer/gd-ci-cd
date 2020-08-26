from django.db import models
from django.utils import timezone


class Contact(models.Model):
    title = models.CharField(max_length=200)
    apartment_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
