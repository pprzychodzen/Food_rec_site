from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    starter = 'st'
    main_course = 'mc'
    soup = 'so'
    dessert = 'de'
    breakfast = 'br'
    supper = 'su'
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=240)

    content = models.TextField(null=True, blank=True)
    picture = models.FileField(upload_to='media/', blank=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    date_last_modified = models.DateTimeField(auto_now=True)
    category_choices = [
        (starter, 'Przystawka'),
        (main_course, 'Danie główne'),
        (soup, 'Zupa'),
        (dessert, 'Deser'),
        (breakfast, 'Śniadanie'),
        (supper, 'Kolacja')
    ]
    category = models.CharField(
        max_length=2,
        choices=category_choices,
        default=main_course
    )
