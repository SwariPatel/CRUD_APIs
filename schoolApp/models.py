from django.db import models

# Create your models here.

class studentRecord(models.Model):
    rollnumber = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.FloatField()
