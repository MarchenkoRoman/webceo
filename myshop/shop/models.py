from decimal import Decimal
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.db.models import F
from django.dispatch import receiver


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=120, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))],
                                verbose_name='цена')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', blank=True)

    class Meta:
        ordering = ('item_name',)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('shop:item_detail',
                       args=[self.item_id])


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=60, verbose_name='Продавец')
    items = models.ManyToManyField(Item, related_name='Товары')

    class Meta:
        ordering = ('employee_name',)

    def __str__(self):
        return self.employee_name


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))],
                                verbose_name='Цена')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return 'Order {}'.format(self.sale_id)

    def get_cost(self):
        return self.price * self.quantity


class PriceHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    validators=[MinValueValidator(Decimal('0.01'))],
                                    verbose_name='Цена')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_date',)


@receiver(post_save, sender=Sale)
def my_handler_sale(sender, instance, **kwargs):
    Item.objects.filter(item_id=instance.item.item_id).update(quantity=F('quantity') - instance.quantity)


@receiver(post_save, sender=Item)
def my_handler(sender, instance, **kwargs):
    PriceHistory.objects.create(item=instance, price=instance.price)