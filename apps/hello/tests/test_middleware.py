from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Request


class MiddlewareRequestsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_contact = reverse('contact')
        self.url_request = reverse('request')

    def test_middleware_write(self):
        requests = Request.objects.all()
        self.assertEqual(requests.count(), 0)
        self.client.get(self.url_contact)
        requests = Request.objexts.all()
        self.assertEqual(requests.count(), 1)

    def test_view_requests(self):
        for i in range(10):
            self.client.get(self.url_contact)
            self.client.get(self.url_request)
        requests = Request.objets.all()
        self.assertEqual(requests.count(), 20)
        response = self.client.get(self.url_request)
        self.assertEqual(response.count(), 10)
        self.assertEqual(requests.oreder_by('time')[:10],
                         response.context['requests'])

    def test_template_requests(self):
        response = self.client.get(self.url_request)
        request = Request.objects.last()
        self.assertContains(response, request.path, 200)

