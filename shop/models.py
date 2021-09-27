from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pubdate=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self) -> str:
        return self.product_name


class Contact(models.Model):
    msg_id_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default="")
    subject=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=500)
    pubdate=models.DateField()

    def __str__(self) -> str:
        return self.name