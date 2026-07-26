from django.db import models
from django.utils.text import slugify

class ProductsCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='productsCategory/', null=True, blank=True)
    icon = models.ImageField(upload_to='productsCategory/categoryIcons/', null=True, blank=True)
    iconMinimal = models.ImageField(upload_to='ProductsCategory/categoryIconsHome/', null=True, blank=True)
    order = models.PositiveBigIntegerField(default=0)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Categoria Prodotto'
        verbose_name_plural = 'Categorie Prodotti'

# --- NUOVO MODELLO PRODOTTO --- #

class Product(models.Model):
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    allergens = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    smallprice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    pricePorKilo = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    variants = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = 'Prodotto'
            verbose_name_plural = 'Prodotti' 

