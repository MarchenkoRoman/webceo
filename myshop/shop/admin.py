from django.contrib import admin
from .models import Item, Employee, Sale


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price', 'quantity', 'available']
    list_filter = ['available']
    list_editable = ['price', 'quantity', 'available']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['item',  'created_date']

