from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db import models

from .models import (Animal, AnimalCondition, AnimalType, AnimalImage,
                     AnimalGroup)


class AdminImageWidget(AdminFileWidget):
    '''Generates Image Preview of StackedInline class'''
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(f'<a href="{image_url}" target="_blank">'
                          f' <img src="{image_url}" alt={file_name}" '
                          f'width="150" height="150"'
                          f'style="object-fit: cover;'
                          f'border-radius: 5px; '
                          f'box-shadow: 0px 2px 17px -4px #6D8291;"/>'
                          f'</a> {_("")} ')
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return format_html(u''.join(output))


class AnimalImageAdminWidget(admin.StackedInline):
    model = AnimalImage
    extra = 1
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}


@admin.register(AnimalGroup)
class AnimalGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'group', 'get_animal_numbers', 'get_icon',
                    'created')
    autocomplete_fields = ['group']
    list_filter = ('group__name',)
    readonly_fields = ('created', 'updated', 'headshot_image')


@admin.register(AnimalCondition)
class AnimalConditionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalImageAdminWidget]
    search_fields = ['animal_type__name']
    autocomplete_fields = ['animal_type', 'conditions']
    list_display = ('animal_type', 'get_conditions', 'description', 'name',
                    'get_images', 'created', 'get_image')
    list_filter = ('animal_type__name',)
    list_display_links = ('name', 'animal_type', 'get_conditions', 'get_image')
    readonly_fields = ('created', 'updated', 'headshot_image')


@admin.register(AnimalImage)
class AnimalImageAdmin(admin.ModelAdmin):
    search_fields = ['animal__animal_type__name', 'animal__name']
    autocomplete_fields = ['animal']
    readonly_fields = ('headshot_image', 'created')
    list_display = ('get_animal', 'get_post_date', 'get_image')
