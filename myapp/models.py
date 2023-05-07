from django.db import models

# Create your models here.

class Student(models.Model):
   username=models.CharField(max_length=100)
   city=models.CharField(max_length=50)
   state=models.CharField(max_length=50)
   status=models.BooleanField(default=True)
   
   def __str__(self):
      return self.username