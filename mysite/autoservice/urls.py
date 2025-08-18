from django.urls import path
from .views import index, cars, car, search
from .views import (OrderListView,
                    OrderDetailView,
                    UserOrderListView,
                    SignUpView,
                    ProfileUpdateView,
                    OrderCreateView,
                    OrderUpdateView,
                    OrderDeleteView,
                    OrderLineCreateView,
                    OrderLineUpdateView,
                    OrderLineDeleteView)

urlpatterns = [
    path('', index, name="index"),
    path('cars', cars, name="cars"),
    path('cars/<int:car_id>', car, name="car"),
    path('search/', search, name="search"),
    path('signup.html/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('orders/', OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>', OrderDetailView.as_view(), name="order"),
    path('userorders/', UserOrderListView.as_view(), name="user_orders"),
    path('orders/new', OrderCreateView.as_view(), name="order_new"),
    path('orders/<int:pk>/edit', OrderUpdateView.as_view(), name="order_edit"),
    path('orders/<int:pk>/delete', OrderDeleteView.as_view(), name="order_delete"),
    path('orders/<int:pk>/newline', OrderLineCreateView.as_view(), name="orderline_new"),
    path('orderline/<int:pk>/edit', OrderLineUpdateView.as_view(), name="orderline_edit"),
    path('orderline/<int:pk>/delete', OrderLineDeleteView.as_view(), name="orderline_delete"),
]