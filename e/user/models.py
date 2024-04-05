from django.db import models


# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=100)
    password = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(null=True, blank=True)
    ph = models.CharField(null=True, blank=True, max_length=10)
    add = models.CharField(null=True, blank=True, max_length=100)


def __str__(self):
    return self.name


class prd(models.Model):
    id = models.AutoField(primary_key=True)
    prd_name = models.CharField(null=True, blank=True, max_length=100)
    price = models.CharField(null=True, blank=True, max_length=100)
    description = models.CharField(null=True, blank=True,max_length=100)
    prd_pric = models.ImageField(upload_to='media/', blank=True, null=True)


def __str__(self):
    return prd.name

