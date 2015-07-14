from django.contrib import admin
from .models import Item
from .models import Brand
from .models import Category
from .models import ProductIdPrefix
from .models import BaseItem


class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


class BaseItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'sku', 'brand', 'categories',
                    'expires_in', 'created', 'modified')

    # search fields help text is in inventory/templates/admin/search_form.html
    search_fields = ['name', 'category__name', 'brand__name', 'expires_in',
                     'sku', 'expires_in', 'description',
                     'product_id_prefix__name']
    list_filter = ('brand', 'category')
    readonly_fields = ('owner',)

    # get_categories function renamed to categories
    def categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

class ItemAdmin(admin.ModelAdmin):
    fields = ('base_item', 'product_id', 'expired',
              'location',)
    readonly_fields = ('product_id', 'expired', 'owner')
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

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


class ProductIdPrefixAdmin(admin.ModelAdmin):
    readonly_fields = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BaseItem, BaseItemAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ProductIdPrefix, ProductIdPrefixAdmin)



