from django.db import models

# Create your models here.

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    yazar = models.CharField(max_length=34)
    date = models.DateTimeField(auto_now=True)
