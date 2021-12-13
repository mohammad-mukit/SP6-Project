from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    payment = models.CharField(max_length=20)

    def __str__(self):
        return self.name