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

# ViewSet will automatically create views for <model> list
# and <model> detail along with the standardized urls
# e.g Brand class will have ..../brand/ and ..../brand/<pk> urls
# showing the list and the details of an item respectively


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'base_items', 'brands', 'categories',
                     'items')


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')


class BrandCreate(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'owner')


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseItemList(generics.ListAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'sku', 'product_id_prefix', 'brand__name',
                     'category__name', 'description', 'owner__username',
                     'expires_in')


class BaseItemCreate(generics.CreateAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemCreateSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseItem.objects.all()
    serializer_class = serializers.BaseItemCreateSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def get_queryset(self):
        query = self.kwargs['pk']
        self.queryset = BaseItem.objects.get(id=query)
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


class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemCreateSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    base_item = serializers.BaseItemCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'type', 'address', 'owner')


class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('item', 'destination', 'items_count', 'origin', 'owner')


class TransactionCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionCreateSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
