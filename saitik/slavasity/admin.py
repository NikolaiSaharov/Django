from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass