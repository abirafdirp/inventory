from django.contrib import admin
from .models import Location, Transaction
from items.models import Item
# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    readonly_fields = ('expired',)

class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline
    ]

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Transaction, TransactionAdmin)
