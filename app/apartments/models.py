from django.db import models
from realtor.models import Realtor
from datetime import datetime
# from django.contrib.auth.models import User
from django.conf import settings


class Apartments(models.Model):
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    region = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    rooms = models.IntegerField(blank=True, null=True)
    square_live = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True)
    square_all = models.DecimalField(max_digits=5, decimal_places=1)
    floor = models.IntegerField(blank=True, null=True)
    apartment_type = models.ForeignKey(
        'ApartmentType', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)
    photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_7 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    realtor = models.ForeignKey(
        Realtor, on_delete=models.DO_NOTHING, blank=True, null=True)
    favorits = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'apartment'
        verbose_name_plural = 'apartments'


class ApartmentType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

