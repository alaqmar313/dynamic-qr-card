from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'created_at')
    readonly_fields = ('id', 'created_at')
