from djongo import models
from django.contrib.auth.models import User
# Create your models here.
# Product Model
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    # _id=models.ObjectIdField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=200,default="")
    category=models.CharField(max_length=20,choices=(
        ("Electronic","Electronic"),
        ("Fashion","Fashion"),
        ("Education","Education"),
        ("Vehicle","Vehicles")
    ))
    price=models.DecimalField(max_digits=10,decimal_places=2,default="")
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="media/images",default="")
    def __str__(self):
        return f"{self.name} {self.category}"


# End product 

# Contact model
class Contact(models.Model):
    # id=models.AutoField(primary_key=True)
    _id=models.ObjectIdField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    msg=models.CharField(max_length=300,default="")

    def __str__(self):
        return f"{self.name} {self.email}"
# End contact

class Address(models.Model):
    address_id=models.ObjectIdField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    mobile=models.CharField(max_length=20,help_text="+12345678")
    email=models.CharField(max_length=50,unique=True)
    province=models.CharField(max_length=50,choices=(
       ("Azad Kashmir","Azad Kashmir"),
       ("Balochistan","Balochistan"),
       ("Islamabad","Islamabad"),
       ("KPK","KPK"),
       ("Punjab","Punjab"),
       ("Sindh","Sindh")
    ))
    city=models.CharField(max_length=50,choices=(
       ("haripur","haripur"),
        ("Abbottbad","Abbottabad"),
       ("Mansehera","Mansehra"),
       ("Hattar","Hattar"),
       ("Ghazi","Ghazi")
    ))
    area=models.CharField(max_length=50,choices=(
       ("Pharhala","Pharhala"),
       ("K.T.S","K.T.S"),
       ("Amir khan plaza","Amir Khan Plaza")
    ))

