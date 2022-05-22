from django.db import models
import datetime
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=50)
    type= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    percent_off = models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="asc/media",default="")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    Status = (
        ('Pending', 'Pending'),
        ('Recived', 'Recived')
    )
    order_id = models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    fullname= models.CharField(max_length=50, default="")
    address= models.CharField(max_length=500, default="")
    city= models.CharField(max_length=100, default="")
    phone=models.IntegerField(default=0)
    qty=models.IntegerField(default=0)
    cnic = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    STATUS = models.CharField(max_length=50, null=True, choices=Status,default='Pending')
    order_time = models.DateTimeField(default=datetime.datetime.today(), null=True)


    def __str__(self):
        return self.fullname

class Deliver(models.Model):
    deliver_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    phone = models.IntegerField(default=0)
    cnic = models.IntegerField(default=0)
    city = models.CharField(max_length=200, default="")
    user = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=8, default="")
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.fullname


class complete(models.Model):
    deliverd_time = models.DateTimeField(default=datetime.datetime.today(),null=True)
    deliver_cnic = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default="")
    order_id = models.IntegerField(default=0)
    received_money = models.IntegerField(default=0)
    def __str__(self):
        return self.city