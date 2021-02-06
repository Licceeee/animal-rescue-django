from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db import models

from .models import (Animal, AnimalCondition, AnimalType, AnimalImage)


class AdminImageWidget(AdminFileWidget):
    '''Generates Image Preview of StackedInline class'''
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(f'<a href="{image_url}" target="_blank">'
                          f' <img src="{image_url}" alt={file_name}" '
                          f'width="150" height="150"  style="object-fit:'
                          f' cover;"/></a> {_("")} ')
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return format_html(u''.join(output))


class AnimalImageAdminWidget(admin.StackedInline):
    model = AnimalImage
    extra = 1
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(AnimalCondition)
class AnimalConditionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'description', 'created')
    readonly_fields = ('created', 'updated')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalImageAdminWidget]
    search_fields = ['_type']
    autocomplete_fields = ['_type', 'conditions']
    list_display = ('_type', 'get_conditions', 'description', 'name',
                    'get_image', 'created')
    readonly_fields = ('created', 'updated', 'headshot_image')


@admin.register(AnimalImage)
class AnimalImageAdmin(admin.ModelAdmin):
    search_fields = ['animal___type__name', 'animal__name']
    autocomplete_fields = ['animal']
    readonly_fields = ('headshot_image', 'created')
    list_display = ('get_animal', 'get_post_date', 'get_image')
