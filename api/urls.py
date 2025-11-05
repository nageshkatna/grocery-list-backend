from rest_framework.routers import DefaultRouter

from api.api_viewsets.viewsets import GroceryItemViewSet


router = DefaultRouter()
router.register(r'groceryItems', GroceryItemViewSet, basename='groceryitem')

urlpatterns = router.urls
