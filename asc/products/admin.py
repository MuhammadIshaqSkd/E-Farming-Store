from django.contrib import admin

# Register your models here.
from .models import Product,Order,Deliver , complete

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Deliver)
admin.site.register(complete)

