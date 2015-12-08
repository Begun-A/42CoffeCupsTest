from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Contact


class TestContactData(TestCase):
    """Tests contact page
    """
    fixtures = ['hello_fixture.json']

    def setUp(self):
        # remember url
        self.url = reverse('contact')
        # remember test browser
        self.client = Client()

    def test_fixtures(self):
        """Test, if db has more then 1 enter
        """
        self.assertEqual(Contact.objects.count(), 1)

    def test_contact_data(self):
        """Test response contact data
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        contact = Contact.objects.first()
        self.assertEqual(contact, response.context['contact'])
