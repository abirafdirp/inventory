from django.contrib import admin
from .models import Brand, Category, Item
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'brand', 'categories', 'expireable',
                    'expires_on', 'created','modified')
    search_fields = ['name']
    list_filter =  ('expireable', 'brand', 'category')

    #a get_categories function renamed to categories
    def categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)

