from django.contrib import admin
from .models import Musician, Album
admin.site.site_header = "Admin Tutorial By Chetan"


def remove_instrument(modeladmin, request, queryset):
    queryset.update(instrument='')


remove_instrument.short_description = "Remove instrument"


class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'instrument')
    list_filter = ('instrument', )
    actions = [remove_instrument]


admin.site.register(Musician, MusicianAdmin)


