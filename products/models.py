from django.db import models

# Create your models here.
class Products(models.Model):
    """
    Products Model
    Defines the attributes of a product
    """
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name + ' is added.'
