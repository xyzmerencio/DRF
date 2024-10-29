from django.contrib import admin
from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "url")
    
class AvaAdmin(admin.ModelAdmin):
    list_display = ("curso", "avaliacao")