from django.contrib import admin

from api.models import Order, Client, Driver


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	search_fields = ['client']


@admin.register(Client)
class OrderAdmin(admin.ModelAdmin):
	search_fields = ['user']


@admin.register(Driver)
class OrderAdmin(admin.ModelAdmin):
	search_fields = ['driver']
