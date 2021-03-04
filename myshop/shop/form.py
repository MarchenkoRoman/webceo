from django import forms
from .models import Employee

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]

class CreateSaleForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="Choose Employee")
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, error_messages='')
