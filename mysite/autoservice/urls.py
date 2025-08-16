from django.contrib import admin
from django.urls import path, include
from .views import index, cars, car
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('', index, name="index"),
    path('cars', cars, name="cars"),
    path('cars/<int:car_id>', car, name="car"),
    path('orders/', OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>', OrderDetailView.as_view(), name="order"),
]