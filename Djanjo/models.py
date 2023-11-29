from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=200,default="")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # date=models.DateField()
    image=models.ImageField(upload_to="product/images")

    def __str__(self):
        return self.name