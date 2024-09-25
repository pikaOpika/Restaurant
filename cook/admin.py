from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from cook.models import Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    pass
