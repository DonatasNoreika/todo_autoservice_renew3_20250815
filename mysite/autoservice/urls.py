from django.contrib import admin
from django.urls import path, include
from .views import index, cars, car, search
from .views import OrderListView, OrderDetailView, UserOrderListView, SignUpView

urlpatterns = [
    path('', index, name="index"),
    path('cars', cars, name="cars"),
    path('cars/<int:car_id>', car, name="car"),
    path('search/', search, name="search"),
    path('signup.html/', SignUpView.as_view(), name='signup'),
    path('orders/', OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>', OrderDetailView.as_view(), name="order"),
    path('userorders/', UserOrderListView.as_view(), name="user_orders"),
]