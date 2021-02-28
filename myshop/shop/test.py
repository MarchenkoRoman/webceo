from django.test  import TestCase
from .models import Item, Employee, Sale


class ItemListTest(TestCase):
    fixtures = ["shop_models"]

    def test_200(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_data_item(self):
        item = Item.objects.get(pk=1)
        self.assertTrue(item.available)

    def test_data_employee(self):
        employee = Employee.objects.get(pk=1)
        self.assertEqual(employee.employee_name, "Nikoloy")