from django.db.models.signals import post_save, pre_save
from django.db.models import F
from django.dispatch import receiver

from .models import Item, PriceHistory, Sale


@receiver(post_save, sender=Sale)
def my_handler_sale(sender, instance, **kwargs):
    Item.objects.filter(item_id=instance.item.item_id).update(quantity=F('quantity') - instance.quantity)


@receiver(pre_save, sender=Item)
def get_price_on_pre_save(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        instance.__original_price = obj.price


@receiver(post_save, sender=Item)
def check_price_post_save(sender, instance, created, **kwargs):
    if not created:
        if not instance.__original_price == sender.objects.get(pk=instance.pk).price:
            PriceHistory.objects.create(item=instance, price=instance.price)