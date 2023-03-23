from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    note = models.TextField(max_length=300)
    id = str(user) + str(date)