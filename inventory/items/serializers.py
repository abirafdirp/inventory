from rest_framework import serializers
from rest_framework import permissions
from .models import Item, Brand, Category, ProductIdPrefix, BaseItem
from inventory.users.models import User
from transaction.models import Location
from django.forms import widgets


class BrandSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Brand
        depth = 1
        field = ('name', 'owner')

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Category
        depth = 1
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

    class Meta:
        model = BaseItem
        # fields added for verbosity
        fields = ('name', 'created', 'modified', 'sku', 'product_id_prefix', 'brand',
                'category', 'description', 'image', 'expires_in', 'owner'
        )

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Item
        depth = 2
        # fields added for verbosity
        fields = ('base_item', 'product_id', 'expiration_date', 'expired', 'location', 'owner')
        read_only_fields = ('expiration_date', 'expired')

class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Location
        depth = 1
        fields = ('name', 'type', 'address', 'owner')

class UserSerializer(serializers.ModelSerializer):
    base_items = BaseItemSerializer()
    brands = BrandSerializer()
    categories = CategorySerializer()
    items = ItemSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'base_items', 'brands', 'categories', 'items')


