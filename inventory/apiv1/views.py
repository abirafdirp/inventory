from rest_framework import permissions
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from items.models import Item
from items.models import Brand
from items.models import Category
from items.models import BaseItem
from transaction.models import Location
from transaction.models import Transaction
from . import serializers
from .permissions import IsOwnerOrReadOnly


from inventory.users.models import User

# model that does not have foreign key does not have CRUD serializers
# list and CRUD serializers must be separated in order to format the JSON 


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'base_items', 'brands', 'categories',
                     'items')


# brand does not have foreignkey
class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')


class BrandCreate(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BrandRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BrandSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = Brand.objects.filter(id=query)
        return self.queryset


# category does not have foreignkey
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')


class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = Category.objects.filter(id=query)
        return self.queryset


class BaseItemList(generics.ListAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'sku', 'product_id_prefix', 'brand__name',
                     'category__name', 'description', 'owner__username',
                     'expires_in')


class BaseItemCreate(generics.ListCreateAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemCRUDSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BaseItemCRUDSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = BaseItem.objects.filter(id=query)
        return self.queryset

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('base_item__name', 'product_id', 'expiration_date',
                     'owner__username', 'location__name', 'expired')


class ItemCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemCRUDSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    base_item = serializers.BaseItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ItemCRUDSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    base_item = serializers.BaseItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = Item.objects.filter(id=query)
        return self.queryset


# location does not have foreign key
class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'address', 'owner')


class LocationCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LocationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LocationSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = Location.objects.filter(id=query)
        return self.queryset


class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('item', 'destination', 'items_count', 'origin', 'owner')


class TransactionCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionCRUDSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TransactionCRUDSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = Transaction.objects.filter(id=query)
        return self.queryset
    

@api_view(('GET',))
def api_root(request):
    return Response({
        'categories': reverse('apiv1:category-list', request=request),
        'create category': reverse('apiv1:category-create',
                                   request=request),

        'base items': reverse('apiv1:baseitem-list', request=request),
        'create base item': reverse('apiv1:baseitem-create',
                                    request=request),

        'brands': reverse('apiv1:brand-list', request=request),
        'create brand': reverse('apiv1:brand-create', request=request),

        'items': reverse('apiv1:item-list', request=request),
        'create item': reverse('apiv1:item-create', request=request),

        'locations': reverse('apiv1:location-list', request=request),
        'create location': reverse('apiv1:location-create',
                                   request=request),

        'transactions': reverse('apiv1:transaction-list', request=request),
        'create transaction': reverse('apiv1:transaction-create',
                                      request=request),
        })
