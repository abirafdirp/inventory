from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Item
from .models import BaseItem
from .models import Category
from .models import Brand
from .serializers import ItemSerializer
from .serializers import BrandSerializer
from .serializers import CategorySerializer
from .serializers import BaseItemSerializer
from .permissions import IsOwnerOrReadOnly

# ViewSet will automatically create views for <model> list
# and <model> detail along with the standardized urls
# e.g Brand class will have ..../brand/ and ..../brand/<pk> urls
# showing the list and the details of an item respectively

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BaseItemViewSet(viewsets.ModelViewSet):
    queryset = BaseItem.objects.all()
    serializer_class = BaseItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)