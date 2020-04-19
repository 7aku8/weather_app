from django.test import SimpleTestCase, Client
from django.urls import reverse
from urllib.error import HTTPError


class ViewTestCase(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('weather:index')
        self.valid_city = {
            'city': 'Rzeszow',
        }
        self.invalid_city = {
            'city': 'Reszdgwsw',
        }

    def test_index_response_without_data(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_index_response_vaild_city(self):
        response = self.client.post(self.url, self.valid_city)

        self.assertEqual(response.status_code, 200)

    def test_index_response_invalid_city(self):
        response = self.client.post(self.url, self.invalid_city)

        self.assertRaises(HTTPError, response)
