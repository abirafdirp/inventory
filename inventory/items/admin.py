from django.contrib import admin
from .models import Brand, Category, BaseItem, Item, ProductIdPrefix
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class BaseItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'brand', 'categories', 'expireable',
                    'expires_in', 'created','modified')

    # search fields help text is in inventory/templates/admin/search_form.html
    search_fields = ['name', 'category__name', 'brand__name','expires_in']
    list_filter =  ('expireable', 'brand', 'category')

    # get_categories function renamed to categories
    def categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])

class ItemAdmin(admin.ModelAdmin):
    pass
class ProductIdPrefixAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BaseItem, BaseItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ProductIdPrefix, ProductIdPrefixAdmin)

