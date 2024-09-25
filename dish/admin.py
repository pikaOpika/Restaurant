from django.contrib import admin
from dish.models import Dish, DishType


@admin.site.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.site.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass
