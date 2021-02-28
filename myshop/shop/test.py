from django.test  import TestCase
from .models import Item


class ItemListTest(TestCase):
    @classmethod
    def set_up_test_data(self):
        Item.objects.create(item_name='Chips', quantity=60, price=1000, description='XXX', available=True)

    def test_200(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
