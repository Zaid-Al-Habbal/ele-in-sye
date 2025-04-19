from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from categories import views

urlpatterns = [
    # path('', views.category_list),
    path('', views.CategoryList.as_view()),
    path('<pk>/', views.category_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
