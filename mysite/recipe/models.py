from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# class Recipe(models.Model):
#     starter = 'st'
#     main_course = 'mc'
#     soup = 'so'
#     dessert = 'de'
#     breakfast = 'br'
#     supper = 'su'
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=240)
#
#     content = models.TextField(null=True, blank=True)
#     picture = models.FileField(upload_to='media/', blank=True)
#     date_of_creation = models.DateTimeField(default=timezone.now)
#     date_last_modified = models.DateTimeField(auto_now=True)
#     category_choices = [
#         (starter, 'Przystawka'),
#         (main_course, 'Danie główne'),
#         (soup, 'Zupa'),
#         (dessert, 'Deser'),
#         (breakfast, 'Śniadanie'),
#         (supper, 'Kolacja')
#     ]
#     category = models.CharField(
#         max_length=2,
#         choices=category_choices,
#         default=main_course
#     )


class RecipeCategory(models.Model):
    recipe_category = models.CharField(max_length=200)
    recipe_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Food Categories"

    def __str__(self):
        return self.recipe_category


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200, default='1')
    recipe_content = models.TextField(default='1')
    recipe_published = models.DateTimeField('data published', default=now)
    recipe_category = models.ForeignKey(RecipeCategory, default=1, verbose_name="Food Categories",
                                        on_delete=models.SET_DEFAULT)
    recipe_slug = models.CharField(max_length=200, default=recipe_title)

    def __str__(self):
        return self.recipe_title
