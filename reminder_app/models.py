from django.db import models
from django.contrib.auth.models import User

# Create your models(classes) here.
# This will determine how the data is stored in a database.
# The class will be your table more or less.


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='default@example.com')
    description = models.TextField(blank=True)
    reminder_time = models.DateTimeField()
    interval = models.PositiveIntegerField()
