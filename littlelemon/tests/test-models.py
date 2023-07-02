# from django.test import TestCase
# from .models import MenuItem

# #TestCase class
# class MenuItemTest(TestCase):
#   def test_get_item(self):
#    item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
#    self.assertEqual(item, "IceCream : 80")

from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name='Menu 1', price=10.99)
        Menu.objects.create(name='Menu 2', price=8.99)
        Menu.objects.create(name='Menu 3', price=12.99)

    def test_getall(self):
        # Retrieve all the Menu objects
        url = reverse('menu-list')
        client = APIClient()
        response = client.get(url, format='json')

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the retrieved objects
        serialized_data = [
            {
                'name': 'Menu 1',
                'price': '10.99',
            },
            {
                'name': 'Menu 2',
                'price': '8.99',
            },
            {
                'name': 'Menu 3',
                'price': '12.99',
            }
        ]

        # Check if the serialized data matches the response data
        self.assertEqual(response.data, serialized_data)

