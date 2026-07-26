from rest_framework import serializers
from .models import ProductsCategory, Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory
        fields = '__all__'

# Aggiungi questo blocco per i prodotti singoli
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'