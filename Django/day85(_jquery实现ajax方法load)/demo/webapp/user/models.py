from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=100,unique=True)
    upwd = models.CharField(max_length=48)
