from django.contrib import admin
from .models import Headline


class EvNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'title', 'image', 'url',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'date', 'title',)
    list_filter = ('date',)


admin.site.register(Headline, EvNewsAdmin)
