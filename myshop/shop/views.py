from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView
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


class ItemDetail(FormView):
    form_class = CreateSaleForm
    template_name = 'product/detail.html'
    success_url = '/'

    def setup(self, request, *args, **kwargs):
        super(ItemDetail, self).setup(request, *args, **kwargs)
        self.item = Item.objects.get(pk=self.kwargs['pk'])


    def get_form_kwargs(self):
        kwargs = super(ItemDetail, self).get_form_kwargs()
        kwargs['item'] = self.item
        return kwargs

    def form_valid(self, form):
        super(ItemDetail, self).form_valid(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            self.form_invalid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. ")


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


