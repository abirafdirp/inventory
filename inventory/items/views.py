from rest_framework import permissions
from rest_framework import filters
from rest_framework import generics
from .models import Item
from .models import BaseItem
from .models import Category
from .models import Brand
from .models import ProductIdPrefix
from transaction.models import Location
from transaction.models import Transaction
from items import serializers
from .permissions import IsOwnerOrReadOnly
from inventory.users.models import User

# ViewSet will automatically create views for <model> list
# and <model> detail along with the standardized urls
# e.g Brand class will have ..../brand/ and ..../brand/<pk> urls
# showing the list and the details of an item respectively

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'base_items', 'brands', 'categories', 'items')

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BrandCreate(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BaseItemList(generics.ListAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'sku', 'product_id_prefix', 'brand__name', 'category__name', 'description',
                     'owner__username', 'expires_in')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BaseItemCreate(generics.CreateAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemCreateSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    base_item = serializers.BaseItemSerializer()
    filter_fields = ('base_item', 'product_id', 'expiration_date', 'owner', 'location')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemCreateSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    base_item = serializers.BaseItemCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductIdPrefixList(generics.ListAPIView):
    queryset = ProductIdPrefix.objects.all()
    serializer_class = serializers.ProductIdPrefixSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name','owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductIdPrefixCreate(generics.CreateAPIView):
    queryset = ProductIdPrefix.objects.all()
    serializer_class = serializers.ProductIdPrefixSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'address', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('items', 'destination', 'origin', 'owner')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TransactionCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionCreateSerializer
    permission_classes = (permissions.IsAuthenticated,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

