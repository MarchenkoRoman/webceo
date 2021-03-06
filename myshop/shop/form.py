from django import forms
from django.core.exceptions import ValidationError
from .models import Employee, Sale, Item


class CreateSaleForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="Choose Employee")
    quantity = forms.IntegerField(min_value=1)

    def __init__(self, item, *args, **kwargs):
        self.item = item
        super(CreateSaleForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].max_value = Item.objects.get(item_id=item.item_id).quantity

    def clean_quantity(self):
        qty = self.cleaned_data['quantity']
        if qty > Item.objects.get(item_id=self.item.item_id).quantity:
            raise ValidationError("We don`t have much quantity")
        return qty

    def save(self):
        Sale.objects.create(
                            item=self.item,
                            quantity=int(self.cleaned_data['quantity']),
                            employee=self.cleaned_data['employee'],
                            price=self.item.price)
