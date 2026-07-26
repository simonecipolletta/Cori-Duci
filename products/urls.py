from django.urls import path
from .views import ProductsList, ProductListView 

urlpatterns = [
    path('categorie/', ProductsList.as_view(), name='category_list'),
    path('prodotti/', ProductListView.as_view(), name='product_list'), 
]