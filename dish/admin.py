from django.contrib import admin
from dish.models import Dish, DishType


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass
