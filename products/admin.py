from django.contrib import admin
from .models import ProductsCategory
from .models import Product

@admin.register(ProductsCategory)
class ProductsCategory(admin.ModelAdmin):
    list_display = ('name', 'order', 'slug')
    search_fields = ('name',)
    ordering = ('order',)
    prepopulated_fields = {'slug': ('name',)} 

    fieldsets = (
        (None, {
            # Nota: ho rimosso 'description' perché non esiste nel modello
            # ho aggiunto 'icon' perché l'hai definita nel modello
            'fields': ('name', 'slug', 'image', 'icon', 'iconMinimal', 'order')
        }),
    )

@admin.register(Product)
class Product(admin.ModelAdmin):
    # Colonne che vedrai nella tabella riassuntiva
    list_display = ('name', 'category', 'price', 'smallprice')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('category', 'name')