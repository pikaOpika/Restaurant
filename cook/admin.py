from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from cook.models import Cook


@admin.site.register(Cook)
class CookAdmin(UserAdmin):
    pass
