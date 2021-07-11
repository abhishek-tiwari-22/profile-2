from django.db import models
from django.contrib import admin

class Details(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField(max_length=1000)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    dob=models.DateField()

    def __str__(self):
        return str(self.id)+"    "+self.name
