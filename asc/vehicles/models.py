from django.db import models
import datetime

# Create your models here.


class vehicle(models.Model):
    type = (
        ('Vehicle', 'Vehicle'),
        ('Tool', 'Tool'),
        ('Drone', 'Drone')
    )
    vehicle_id = models.AutoField
    vehicle_name=models.CharField(max_length=50)
    TYPE = models.CharField(max_length=50, null=True, choices=type, default='Vehicle')
    rent_price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="asc/media",default="")


    def __str__(self):
        return self.vehicle_name

class tool(models.Model):
    type = (
        ('Vehicle', 'Vehicle'),
        ('Tool', 'Tool'),
        ('Drone', 'Drone')
    )
    tool_id = models.AutoField
    tool_name=models.CharField(max_length=50)
    TYPE = models.CharField(max_length=50, null=True, choices=type, default='Tool')
    rent_price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="asc/media",default="")


    def __str__(self):
        return self.tool_name

class drone(models.Model):
    type = (
        ('Vehicle', 'Vehicle'),
        ('Tool', 'Tool'),
        ('Drone', 'Drone')
    )
    drone_id = models.AutoField
    drone_name=models.CharField(max_length=50)
    TYPE = models.CharField(max_length=50, null=True, choices=type, default='Drone')
    rent_price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="asc/media",default="")


    def __str__(self):
        return self.drone_name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    vname = models.CharField(max_length=50)
    address= models.CharField(max_length=500, default="")
    phone=models.IntegerField(default=0)
    cnic = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    branch= models.CharField(max_length=500, default="")
    booking_time = models.DateTimeField(default=datetime.datetime.today(), null=True)


    def __str__(self):
        return self.name

class branche(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name=models.CharField(max_length=50)
    address= models.CharField(max_length=500, default="")
    office_timing= models.CharField(max_length=500, default="")
    branch_tele=models.IntegerField(default=0)
    create_time = models.DateTimeField(default=datetime.datetime.today(), null=True)

    def __str__(self):
        return self.branch_name

class complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone= models.IntegerField(default=0)
    complaint_type= models.CharField(max_length=20, default="")
    complaint_details= models.CharField(max_length=1000, default="")
    complaint_time = models.DateTimeField(default=datetime.datetime.today(), null=True)

    def __str__(self):
        return self.name