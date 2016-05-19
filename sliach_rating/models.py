from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class State(models.Model):
    country = models.CharField(max_length=200, default="USA")
    state = models.CharField(max_length=200)
    
    def __str__(self):
        return self.state


class Sluchim(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100, default="bob")
    phone = models.CharField(max_length=35, default="999-999-99999")
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    picture = models.ImageField(default='./nick_XBVHPAg.jpg ')
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

