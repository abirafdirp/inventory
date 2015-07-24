from rest_framework import serializers
from rest_framework import permissions
from items.models import Item
from items.models import Brand
from items.models import Category
from items.models import BaseItem
from inventory.users.models import User
from transaction.models import Location
from transaction.models import Transaction

"""
some model will have two serializers, because somehow
I can't make a viewset to display a model in detail (nested related model)
and properly give options (list e.g categories) in the form at the same time.
So I create one serializer for viewset that will have two urls, the name
of the model itself and .../<model_name>/<pk>/ automatically mapped
using router. The create page is using generics.CreateAPIView and the
url is .../<model_name>/<pk>/ and must be manually mapped.

model with no foreign key is still using viewset because there is no
nested model in the JSON.
"""



class BrandSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Brand
        field = ('name', 'owner')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Category
        field = ('name', 'owner')


class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Location
        depth = 1
        fields = ('name', 'type', 'address', 'owner')


class BaseItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    # nested related's model class must be initialized
    brand = BrandSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = BaseItem

        # fields added for verbosity
        fields = ('id', 'name', 'created', 'modified', 'sku',
                  'product_id_prefix', 'brand', 'category',
                  'description', 'image', 'expires_in', 'owner')


class BaseItemCRUDSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = BaseItem

        # fields added for verbosity
        fields = ('name', 'created', 'modified', 'sku', 'product_id_prefix',
                  'brand', 'category', 'description', 'image', 'expires_in',
                  'owner')


class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    item = BaseItemSerializer()
    origin = LocationSerializer()
    destination = LocationSerializer()

    class Meta:
        model = Transaction

        # fields added for verbosity
        fields = ('id', 'item', 'items_count', 'origin', 'destination', 'owner',
                  'date_time')


class TransactionCRUDSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Transaction

        # fields added for verbosity
        fields = ('item', 'items_count', 'origin', 'destination', 'owner')
        read_only_fields = ('date_time',)


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    # nested related's model class must be initialized
    base_item = BaseItemSerializer()
    location = LocationSerializer()

    class Meta:
        model = Item

        # fields added for verbosity
        fields = ('id', 'base_item', 'product_id', 'expiration_date', 'expired',
                  'location', 'owner')


class ItemCRUDSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = Item

        # fields added for verbosity
        fields = ('base_item', 'product_id', 'location', 'owner')
        read_only_fields = ('expiration_date', 'expired')


class UserSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticated,)
    base_items = BaseItemSerializer(many=True)
    brands = BrandSerializer(many=True)
    categories = CategorySerializer(many=True)
    items = ItemSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'base_items', 'brands', 'categories',
                  'items')
