from django.db import models

# Create your models here.
class Info(models.Model):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    email = models.EmailField()
    pass1 = models.CharField( max_length=50)
    pass2 = models.CharField( max_length=50)