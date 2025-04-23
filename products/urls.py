from django.urls import path, include

from rest_framework.routers import DefaultRouter

from products.views import ProductListView, ProductCreateView, ProductEditView

urlpatterns = [
    path('', ProductListView.as_view(), name="list_products"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('<int:pk>/', ProductEditView.as_view(), name='product-detail'),
]
