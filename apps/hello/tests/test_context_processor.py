from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class ContextProcessorsTest(TestCase):
    """Tests context processors"""
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()
        self.url_1 = reverse('contact')
        self.url_2 = reverse('requests')

    def test_settings_proc(self):
        """Test settigs_proc context processor"""
        response = self.client.get(self.url_1)
        self.assertIn('SETTINGS', response.context)
        response = self.client.get(self.url_2)
        self.assertIn('SETTINGS', response.context)
