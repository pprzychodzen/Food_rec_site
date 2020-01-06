from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=240)
    # ingredients = models.

    content = models.TextField(null=True, blank=True)
    picture = models.FileField(upload_to='media/', blank=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    date_last_modified = models.DateTimeField(auto_now=True)
