from django.contrib import admin

# Register your models here.
from .models import vehicle,tool,drone,Booking,branche,complaint

admin.site.register(vehicle)
admin.site.register(tool)
admin.site.register(drone)
admin.site.register(Booking)
admin.site.register(branche)
admin.site.register(complaint)