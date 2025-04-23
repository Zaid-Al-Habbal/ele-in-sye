from django.urls import path, include

from rest_framework.routers import DefaultRouter

from products.views import ProductListView, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # path('', ProductListView.as_view(), name="list_products"),
    path('', include(router.urls))
]
