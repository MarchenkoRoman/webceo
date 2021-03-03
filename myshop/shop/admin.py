from django.contrib import admin
from .models import Item, Employee, Sale, PriceHistory


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price', 'quantity', 'available']
    list_filter = ['available']
    list_editable = ['price', 'quantity', 'available']

    def save_model(self, request, obj, form, change):
        update_fields = []
        for key, value in form.cleaned_data.items():
            try:
                if value != form.initial[key]:
                    update_fields.append(key)
            except KeyError:
                pass
        obj.save(update_fields=update_fields)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['item',  'created_date']


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'item', 'price']