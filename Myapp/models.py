from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

