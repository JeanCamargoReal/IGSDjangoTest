import uuid

from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    departament = models.CharField(max_length=150, blank=True, null=False)
    
    def __str__(self):
        return self.name
