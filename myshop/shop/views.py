from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Item, Sale, PriceHistory
from .form import CreateSaleForm


class ItemList(ListView):
    model = Item
    paginate_by = 8
    context_object_name = "items"
    template_name = "base.html"

    def get_queryset(self):
        queryset = self.model._default_manager.filter(available=True).exclude(quantity=0)
        return queryset


class ItemDetail(FormMixin, DetailView):
    model = Item
    context_object_name = "item"
    template_name = "product/detail.html"
    form_class = CreateSaleForm

    def get_success_url(self):
        return '/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        quantity = form.cleaned_data['quantity']
        employee = form.cleaned_data['employee']
        if self.object.quantity >= quantity:
            Sale.objects.create(item=self.object,
                                quantity=quantity,
                                employee=employee,
                                price=self.object.price)
        else:
            return form
        return super().form_valid(form)


# @render_to("product/detail.html")
# def item_detail(request, item_id):
#     item = get_object_or_404(Item, item_id=item_id, available=True)
#     if request.method == 'POST':
#         form = CreateSaleForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             employee = form.cleaned_data['employee']
#             if item.quantity >= quantity:
#                 Sale.objects.create(item=item,
#                                     quantity=quantity,
#                                     employee=employee,
#                                     price=item.price)
#             return HttpResponseRedirect('/')
#     else:
#         form = CreateSaleForm(request.POST)
#
#     return {"item": item, "form": form}

class SaleList(LoginRequiredMixin, ListView):
    model = Sale
    paginate_by = 5
    context_object_name = "sales"
    template_name = "sale/salelist.html"


class HistoryPrice(LoginRequiredMixin, ListView):
    model = PriceHistory
    paginate_by = 5
    context_object_name = "history_price"
    template_name = "history_price/history_price_list.html"


