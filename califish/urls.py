from django.urls import path
from califish import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product_list/', views.ProductList.as_view(), name='product_list')
]