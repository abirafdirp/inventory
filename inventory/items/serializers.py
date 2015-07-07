from rest_framework import serializers
from .models import Item, Brand, Category, ProductIdPrefix, BaseItem
from transaction.models import Location
from django.forms import widgets

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        field = ('name',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ('name',)

class ProductIdPrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIdPrefix
        field = ('name',)

class BaseItemSerializer(serializers.Serializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    product_id_prefix = ProductIdPrefixSerializer()

    class Meta:
        model = BaseItem

        # fields added for verbosity
        fields = ('name', 'created', 'modified', 'sku', 'product_id_prefix', 'brand',
                'category', 'description', 'image', 'expireable', 'expires_in',
        )

class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = ('name', 'type', 'address')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

        # fields added for verbosity
        fields = ('base_item', 'product_id', 'expiration_date', 'expired', 'location')