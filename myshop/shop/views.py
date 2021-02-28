from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from . models import Item


class ItemList(ListView):
    model = Item
    paginate_by = 8
    context_object_name = "items"
    template_name = "base.html"

    def get_queryset(self):
        queryset = self.model._default_manager.filter(available=True).exclude(quantity=0)
        return queryset

def item_detail(request, item_id):
    item = get_object_or_404(Item, item_id=item_id, available=True)
    return render(request, "product/detail.html", {"item": item,})