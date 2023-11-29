from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=100)
    prize=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to="product/images")

    def __str__(self):
        return self.name.title()
