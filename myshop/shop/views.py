from django.views.generic import ListView
from . models import Item


class ItemList(ListView):
    model = Item
    context_object_name = "items"
    template_name = "base.html"

    def get_queryset(self):
        queryset = self.model._default_manager.filter(available=True).exclude(quantity=0)
        return queryset