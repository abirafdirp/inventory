from django.contrib import admin
from .models import Brand, Category, BaseItem, Item, ProductIdPrefix
# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class BaseItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'sku', 'brand', 'categories',
                    'expires_in', 'created', 'modified')

    # search fields help text is in inventory/templates/admin/search_form.html
    search_fields = ['name', 'category__name', 'brand__name', 'expires_in',
                     'sku', 'expires_in', 'description',
                     'product_id_prefix__name']
    list_filter = ('brand', 'category')

    # get_categories function renamed to categories
    def categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])


class ItemAdmin(admin.ModelAdmin):
    fields = ('base_item', 'product_id', 'expired',
              'location',)
    readonly_fields = ('product_id', 'expired')
    list_display = ('Name', 'SKU', 'product_id', 'location', 'expiration_date',
                    'expired')
    search_fields = ['base_item__name', 'product_id', 'location__name']

    # functions below are renamed for verbosity in admin
    # get sku function renamed to SKU
    def SKU(self, instance):
        return instance.base_item.sku

    # get name function renamed to Name
    def Name(self, instance):
        return instance.base_item.name


class ProductIdPrefixAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BaseItem, BaseItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ProductIdPrefix, ProductIdPrefixAdmin)



