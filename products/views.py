from rest_framework import generics
from .models import ProductsCategory, Product
from .serializers import ProductsSerializer, ProductSerializer

class ProductsList(generics.ListAPIView):
    queryset = ProductsCategory.objects.all().order_by('order')
    serializer_class = ProductsSerializer

# Aggiungi questa vista per mandare i prodotti a Vue
# class Products(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#vedere qual'è meglio tra le due
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
            # Prendiamo tutti i prodotti
            queryset = Product.objects.all()
            
            # Filtriamo se Vue ci manda l'ID nell'URL
            categoria_id = self.request.query_params.get('categoria', None)
            if categoria_id is not None:
                queryset = queryset.filter(category_id=categoria_id)
                
            return queryset