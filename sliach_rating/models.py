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
    phone = models.IntegerField(default=99999999999)
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    picture = models.ImageField(default=None)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

