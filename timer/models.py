from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    types = (
        (0, 'rest'),
        (1, 'work'),
    )
    type = models.IntegerField(choices=types, verbose_name='type', blank=False)
    date = models.DateTimeField(db_index=True, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.IntegerField(null=True)