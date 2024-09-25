from django.contrib import admin
from ingredient.models import Ingredient


@admin.site.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
