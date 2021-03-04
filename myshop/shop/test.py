from django.contrib.auth.models import User
from django.test  import TestCase
from django.test.client import Client
from django.urls import reverse
from django.urls import resolve
import unittest
from .models import Item, Employee, PriceHistory
from .views import  ItemList


class HomePageTest(TestCase):
    """Testing home page"""

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8')
        self.assertIn('<title>This amazing shop</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))


class DetailPageTest(TestCase):
    fixtures = ["shop_models"]

    """Testing detail page"""

    def test_url_resolves_to_detail_page_view(self):
        item1 = Item.objects.get(pk=1)
        url = reverse('shop:item_detail', args=[item1.item_id, ])
        response =self.client.get(url)
        self.assertContains(response, item1.item_name)


class ItemListTest(TestCase):
    fixtures = ["shop_models"]

    def test_data_item(self):
        item = Item.objects.get(pk=1)
        self.assertTrue(item.available)


    def test_data_employee(self):
        employee = Employee.objects.get(pk=1)
        self.assertEqual(employee.employee_name, "Nikoloy")

    def test_assert_contain_item(self):
        response = self.client.get('/')
        item2 = Item.objects.get(pk=2)
        self.assertContains(response, item2.price)
        item1 = Item.objects.get(pk=1)
        self.assertContains(response, item1.item_name)


class HistoryPriceTest(TestCase):
    """Testing  post_save"""
    fixtures = ["shop_models"]
    def set_up(self):
        self.client = Client()
        self.user = User.objects.create('mike', 'tyson@gmail.com', 'miketysonpass')

    def test_post_save_signals(self):
        item = Item.objects.get(pk=1)
        item.price = 1000.00
        item.save()
        hp_price_object = PriceHistory.objects.first()
        self.assertEqual(item.price, hp_price_object.price, msg='All in order')

    def tes_login(self):
        self.client.login(username='mike', password='miketysonpass')
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

