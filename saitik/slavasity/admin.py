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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price', 'created_at', 'status', 'games_list']

    def games_list(self, obj):
        return ", ".join([game.title for game in obj.games.all()])
    games_list.short_description = 'Игры в заказе'


@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'license_key', 'delivery_status']