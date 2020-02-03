from django.shortcuts import render
from django.views.generic.edit import CreateView
from recipe.models import Recipe
from recipe.forms import RecipeForm


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'

