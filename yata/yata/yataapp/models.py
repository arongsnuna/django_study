from django.db import models

from django.contrib.auth.models import User
class Room(models.Model):
    address = models.CharField(max_length=100)
    getDate = models.DateField()
    getTime = models.TimeField()
    MEMBERS_CHOICES={
        ('2','2'),
        ('3','3'),
        ('4','4'),
    }
    member = models.CharField(choices = MEMBERS_CHOICES, max_length=3)
    location = models.CharField(max_length=100)
    captain = models.ForeignKey(User, on_delete=models.CASCADE)
