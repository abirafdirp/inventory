from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .models import Item
from .models import BaseItem
from .models import Category
from .models import Brand
from .models import ProductIdPrefix
from transaction.models import Location
from .serializers import ItemSerializer
from .serializers import BrandSerializer
from .serializers import CategorySerializer
from .serializers import BaseItemSerializer
from .serializers import UserSerializer
from .serializers import ProductIdPrefixSerializer
from .serializers import LocationSerializer
from .permissions import IsOwnerOrReadOnly
from inventory.users.models import User

# ViewSet will automatically create views for <model> list
# and <model> detail along with the standardized urls
# e.g Brand class will have ..../brand/ and ..../brand/<pk> urls
# showing the list and the details of an item respectively

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'base_items', 'brands', 'categories', 'items')

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BaseItemViewSet(viewsets.ModelViewSet):
    queryset = BaseItem.objects.all()
    serializer_class = BaseItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'sku', 'product_id_prefix', 'brand__name', 'category__name', 'description',
                     'owner', 'expires_in')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    base_item = BaseItemSerializer()
    filter_fields = ('base_item', 'product_id', 'expiration_date', 'owner', 'location')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductIdPrefixViewSet(viewsets.ModelViewSet):
    queryset = ProductIdPrefix.objects.all()
    serializer_class = ProductIdPrefixSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name','owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'address', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)