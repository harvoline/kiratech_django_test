from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class InventoryTest(TestCase):

    def test_inventory_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_find_exist_inventory(self):
        response = self.client.get(reverse('show', kwargs={'inventory_id':1}))
        self.assertEqual(response.status_code, 200)

    def test_find_non_exist_inventory(self):
        response = self.client.get(reverse('show', kwargs={'inventory_id':0}))
        self.assertEqual(response.status_code, 404)
