from api.utils import GroceryPagination

from rest_framework import viewsets

from .serializers import GroceryItemSerializer
from api.models import GroceryItem

class GroceryItemViewSet(viewsets.ModelViewSet):
    queryset = GroceryItem.objects.all().order_by('id')
    serializer_class = GroceryItemSerializer
    pagination_class = GroceryPagination

