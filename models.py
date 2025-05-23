from django.db import models

# Create your models here.

class data(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    name = models.CharField(max_length=100)


