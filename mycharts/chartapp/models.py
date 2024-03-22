from django.db import models
# from django.contrib.auth import AbstractUser
from django.db.models import DateTimeField

# Create your models here.

class Product(models.Model):
    # end_year        = models.IntegerField(null=True, blank=True)
    end_year        = models.CharField(max_length=100,null=True, blank=True)
    intensity       = models.IntegerField(null=True, blank=True)
    sector          = models.CharField(max_length=100, null=True, blank=True)
    topic           = models.CharField(max_length=100, null=True, blank=True)
    insight         = models.CharField(max_length=100, null=True, blank=True)
    url             = models.URLField(max_length=100, null=True, blank=True)
    region          = models.CharField(max_length=100, null=True, blank=True)
    start_year      = models.CharField(max_length=100, null=True, blank=True)
    impact          = models.IntegerField(null=True, blank=True)

    added           = models.CharField(max_length=100,null=True, blank=True)
    # added           = models.DateTimeField(null=True, blank=True)
    published       = models.CharField(max_length=100, blank=True, null=True)
    # published       = models.DateTimeField(null=True, blank=True)

    country         = models.CharField(max_length=100, null=True, blank=True)
    relevance       = models.IntegerField(null=True, blank=True)
    pestle          = models.CharField(max_length=100, null=True, blank=True)
    source          = models.CharField(max_length=100, null=True, blank=True)
    title           = models.CharField(max_length=100, null=True, blank=True)
    likelihood      = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.region} - {self.title}'
        # return self.likelihood
    


class Signup(models.Model):
    username    = models.CharField(max_length=50, unique=True)
    email       = models.EmailField(max_length=50, unique=True)
    password    = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.email