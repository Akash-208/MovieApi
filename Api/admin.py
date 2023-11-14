from django.contrib import admin
from . models import MovieData
# Register your models here.

@admin.register(MovieData)
class movieDataAdmin(admin.ModelAdmin):
    list_display = ['id','name','release_year','rating']