from rest_framework import serializers
from rest_framework import permissions
from .models import Item, Brand, Category, ProductIdPrefix, BaseItem
from transaction.models import Location
from django.forms import widgets

"""class Permission():
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)"""

class BrandSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Brand
        field = ('name', 'owner')

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Category
        field = ('name', 'owner')

class ProductIdPrefixSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = ProductIdPrefix
        field = ('name', 'owner')

class BaseItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    brand = BrandSerializer()
    category = CategorySerializer()
    product_id_prefix = ProductIdPrefixSerializer()

    class Meta:
        model = BaseItem

        # fields added for verbosity
        fields = ('name', 'created', 'modified', 'sku', 'product_id_prefix', 'brand',
                'category', 'description', 'image', 'expireable', 'expires_in','owner'
        )

class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Location
        fields = ('name', 'type', 'address')

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Item

        # fields added for verbosity
        fields = ('base_item', 'product_id', 'expiration_date', 'expired', 'location', 'owner')