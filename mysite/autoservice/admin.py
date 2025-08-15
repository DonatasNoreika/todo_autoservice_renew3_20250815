from django.contrib import admin
from .models import Car, Service, Order, OrderLine


# Register your models here.
class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    fields = ['service', 'quantity', 'line_sum']
    readonly_fields = ['line_sum']


class OrderAdmin(admin.ModelAdmin):
    list_display = ["car", "date", "total"]
    inlines = [OrderLineInLine]
    fieldsets = [
        ("General", {"fields": ['car', 'date', 'total']})
    ]
    readonly_fields = ['date', 'total']


class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'license_plate', 'vin_code', 'client_name']
    list_filter = ['client_name', 'make', 'model']
    search_fields = ['license_plate', 'vin_code']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'service', 'quantity', 'line_sum']
    fieldsets = [
        ("General", {"fields": ['order', 'service', 'quantity', 'line_sum']})
    ]
    readonly_fields = ['line_sum']

admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
