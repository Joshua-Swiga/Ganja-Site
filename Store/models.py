from django.db import models


 
class Product(models.Model):
    custom_id = models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_tags = models.CharField(max_length=150, null=True, blank=True)
    product_category = models.CharField(max_length=100, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    available_quantity = models.IntegerField(null=True, blank=True)
    liscence_of_sale = models.URLField(null=True, blank=True)
    product_image = models.ImageField(upload_to='product_information/product_images', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.product_name}: {self.product_description}'
    
class Quality_shelf(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_currency = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_information/quality_shelf')
    category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.product_name}: {self.category}'