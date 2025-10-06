from django.contrib import admin
from .models import *
from transfer.models import *
from django.contrib.auth.models import Group,User

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name','president','coach','found_date','country',)
    search_fields = ('name',)
    list_filter = ('country',)
    ordering = ('found_date',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','position','number','age','price','nation','club',)
    search_fields = ('name',)
    list_filter = ('club','nation','position',)
    ordering = ('number','age','price',)