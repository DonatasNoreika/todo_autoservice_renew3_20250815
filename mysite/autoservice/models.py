from django.db import models


# Create your models here.
class Car(models.Model):
    make = models.CharField(verbose_name="Make", max_length=100)
    model = models.CharField(verbose_name="Model", max_length=100)
    license_plate = models.CharField(verbose_name="License Plate", max_length=10)
    vin_code = models.CharField(verbose_name="VIN Code", max_length=20)
    client_name = models.CharField(verbose_name="Client Name", max_length=50)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"


class Service(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    price = models.FloatField(verbose_name="Price")

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.date}: {self.car}"


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Quantity")

    def __str__(self):
        return f"{self.service.name} - {self.quantity} ({self.order.car})"
