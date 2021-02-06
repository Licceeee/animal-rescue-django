from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ['content', 'sender', 'receiver']
    list_display = ('content', 'sender', 'receiver', 'created')
    autocomplete_fields = ['sender', 'receiver']
    readonly_fields = ('created',)
