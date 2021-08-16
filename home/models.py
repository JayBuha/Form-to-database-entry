from django.db import models

# Create your models here.

class Contact(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    date = models.DateField()

    def __str__(self):
        return self.First_name
    
