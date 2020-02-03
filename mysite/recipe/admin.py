from django.contrib import admin
from .models import Recipe, RecipeCategory
from tinymce.widgets import TinyMCE
from django.db import models


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["recipe_title", "recipe_published"]}),
        ("URL", {"fields": ["recipe_slug"]}),
        ('Category', {"fields": ['recipe_category']}),
        ("Content", {"fields": ["recipe_content"]})
    ]

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}
    }


admin.site.register(RecipeCategory)

admin.site.register(Recipe, RecipeAdmin)