from django.test import RequestFactory, TestCase
from django.urls import reverse
import requests
from .views import InventoryViewSet
# from inventory.views import

# Create your tests here.


class InventoryApiTest(TestCase):
    def setUp(self):

        self.factory = RequestFactory()
        self.view = InventoryViewSet.as_view({'get': 'list'})
        self.uri = '/api/inventory/'

    def test_api_inventory_list(self):
        response = self.client.get('http://127.0.0.1:8020/api/inventory', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_api_find_exist_inventory(self):
        request = self.factory.get(self.uri + "1", follow=True)
        response = self.view(request)

        self.assertEqual(response.status_code, 200)

