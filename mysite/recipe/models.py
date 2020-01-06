from django.db import models


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(null=True)
    title = models.CharField(max_length=300)
