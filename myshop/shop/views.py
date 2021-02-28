from django.shortcuts import render
from annoying.decorators import render_to
from . models import Item


@render_to('base.html')
def item_list(request):
    items = Item.objects.all()
    return {'items': items}