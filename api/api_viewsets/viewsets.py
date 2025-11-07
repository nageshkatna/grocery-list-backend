from api.utils import GroceryPagination

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import GroceryItemSerializer
from api.models import GroceryItem

class GroceryItemViewSet(viewsets.ModelViewSet):
    queryset = GroceryItem.objects.all().order_by('purchased', '-created_at')
    serializer_class = GroceryItemSerializer
    pagination_class = GroceryPagination

    def create(self, request, *args, **kwargs):
        name = request.data.get('name', '').strip()
        existing_item = GroceryItem.objects.filter(name__iexact=name).first()
        
        if existing_item:
            return Response(
                {"error": f"A grocery item with name '{name}' already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

