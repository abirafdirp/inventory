from django.contrib import admin
from .models import Location, Transaction
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Transaction, TransactionAdmin)
