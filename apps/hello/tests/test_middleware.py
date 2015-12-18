import random
from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import RequestLog


class MiddlewareRequestLogsTests(TestCase):
    """Test middleware and requests page
    """

    def setUp(self):
        self.client = Client()
        self.url_contact = reverse('contact')
        self.url_request = reverse('requests')

    def test_middleware_write(self):
        """Test middleware store data
        """
        requests = RequestLog.objects.all()
        self.assertEqual(requests.count(), 0)
        self.client.get(self.url_contact)
        requests = RequestLog.objects.all()
        self.assertEqual(requests.count(), 1)

    def test_view_requests(self):
        """Test requests view
        """
        for i in range(10):
            self.client.get(self.url_contact)
            self.client.get(self.url_request)
        requests = RequestLog.objects.order_by('time')
        self.assertEqual(requests.count(), 20)
        requests = requests.reverse()[:10]
        response = self.client.get(self.url_request)
        self.assertEqual(response.context['request_log'].count(), 10)
        for i in range(0, 10):
            self.assertEqual(response.context['request_log'][i], requests[i])

    def test_template_requests(self):
        """Test requests template
        """
        response = self.client.get(self.url_request)
        request = RequestLog.objects.last()
        self.assertContains(response, request.path)

    def test_view_requests_sort(self):
        """Test requests sort
        """
        for i in range(20):
            RequestLog(remote_addr='/', time=datetime.now(),
                       priority=random.choice((1, 2, 3))).save()

        requests = RequestLog.objects.order_by('-time')[:10]
        response = self.client.get(self.url_request)
        for i in range(10):
            self.assertEqual(response.context['request_log'][i], requests[i])

        self.assertIn("/requests/?order_by=priority", response.content)
        response = self.client.get(self.url_request + "?order_by=priority")
        requests = RequestLog.objects.order_by('priority')[:10]
        for i in range(10):
            self.assertEqual(response.context['request_log'][i], requests[i])

        self.assertIn("/requests/?order_by=-priority", response.content)
        response = self.client.get(self.url_request + "?order_by=-priority")
        requests = RequestLog.objects.order_by('-priority')[:10]
        for i in range(10):
            self.assertEqual(response.context['request_log'][i], requests[i])
