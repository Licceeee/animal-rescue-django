from django.contrib import admin
from django.db import models

from .models import (Animal, AnimalCondition, AnimalType)


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(AnimalCondition)
class AnimalConditionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created')
    readonly_fields = ('created', 'updated')



@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    search_fields = ['type']
    autocomplete_fields = ['type', 'conditions']
    list_display = ('type', 'get_conditions', 'name', 'get_image', 'created')
    readonly_fields = ('created', 'updated', 'headshot_image')


