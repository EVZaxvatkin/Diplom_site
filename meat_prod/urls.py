from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='index'),
    path('category/', views.categories, name = 'category'),

    path('product_list/<int:category_id>/', views.product_list, name = 'product_list'),
    path('product/<int:product_id>/', views.products, name = 'products'),

    ]