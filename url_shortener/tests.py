from django.test import TestCase

from .models import Ad, User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import json

TEST_SIZE = 10


class TestLinkShortener(APITestCase):
    def setUp(self):
        self.ids = list(range(1, 6))
        self.payload_data = {'status': 'оплачено', 'ids': self.ids}
        self.ads = []
        self.user = User.objects.create_user('test_user_1', 'example@test.com', '123')
        # create a set of test ads
        for i in range(TEST_SIZE):
            self.ads.append(Ad.objects.create(title='Test ad {}'.format(i), category='разное', status='отказ', author=self.user)) 

    def test_update_ads_user(self):
        # Invalid case - normal user
        response = self.client.put(
            '/ads/status',
            data=json.dumps(self.payload_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_ads_superuser(self):
        # Correct case - superuser
        self.assertTrue(self.client.login(username='admin', password='123'))
        response = self.client.put(
            '/ads/status',
            data=json.dumps(self.payload_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
