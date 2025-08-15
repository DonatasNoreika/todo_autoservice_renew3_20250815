from django.contrib import admin
from .models import Car, Service, Order, OrderLine

# Register your models here.
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderLine)
