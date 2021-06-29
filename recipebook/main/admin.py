from django.contrib import admin
from .models import Recipes, Ingredients


admin.site.register(Ingredients)
admin.site.register(Recipes)
