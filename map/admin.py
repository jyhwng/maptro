from django.contrib import admin
from .models import Line, Station, Nick, Like
from django.contrib.auth.models import User

@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
    list_display_links = ['name']

@admin.register(Nick)
class NickAdmin(admin.ModelAdmin):
    # list_display = ['name', 'like', 'created_at']
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'user']
    list_display_links = ['nick']
