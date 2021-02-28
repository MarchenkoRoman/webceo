from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from annoying.decorators import render_to
from django.views.generic import ListView
from .models import Item, Sale


class ItemList(ListView):
    model = Item
    paginate_by = 8
    context_object_name = "items"
    template_name = "base.html"

    def get_queryset(self):
        queryset = self.model._default_manager.filter(available=True).exclude(quantity=0)
        return queryset

@render_to("product/detail.html")
def item_detail(request, item_id):
    item = get_object_or_404(Item, item_id=item_id, available=True)
    return {"item": item}

class SaleList(LoginRequiredMixin, ListView):
    model = Sale
    paginate_by = 5
    context_object_name = "sales"
    template_name = "sale/salelist.html"


