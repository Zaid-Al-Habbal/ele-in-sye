from django.urls import path, include

from rest_framework.routers import DefaultRouter

from products.views import ProductListView, ProductCreateView, ProductEditView, ProductShowView

urlpatterns = [
    path('', ProductListView.as_view(), name="list_products"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('<int:pk>/', ProductShowView.as_view(), name='product-detail'),
]
