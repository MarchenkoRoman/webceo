from django.test  import TestCase
from django.urls import resolve
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
    """Testing detail page"""

    def test_url_resolves_to_detail_page_view(self):
        pass



class ItemListTest(TestCase):
    fixtures = ["shop_models"]

    def test_data_item(self):
        item = Item.objects.get(pk=1)
        self.assertTrue(item.available)

    def test_data_employee(self):
        employee = Employee.objects.get(pk=1)
        self.assertEqual(employee.employee_name, "Nikoloy")



class HistoryPriceTest(TestCase):
    """Testing  post_save"""
    fixtures = ["shop_models"]
    def testing_post_save_signals(self):
        item = Item.objects.get(pk=1)
        item.price = 1000.00
        item.save()
        hp_price_object = PriceHistory.objects.first()
        self.assertEqual(item.price, hp_price_object.price, msg='All in order')

