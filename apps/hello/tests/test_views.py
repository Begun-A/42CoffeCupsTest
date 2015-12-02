from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Contact

class TestContactData(TestCase):
    """Tests contact_data view"""
    fixtures = ['initial_data.json']

    def setUp(self):
        # remember url
        self.url = reverse('contact_data')
        # remember test browser
        self.client = Client()

    def test_fixtures(self):
        """Test, if db has more then 1 enter"""
        self.assertEqual(Contact.objects.count(),1)

    def test_contact_data(self):
        """Test response contact data """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

        contact = Contact.objects.first()

        self.assertIn(contact.name, response.content)
        self.assertIn(contact.surname, response.content)
        self.assertIn(contact.birth_day, response.content)
        self.assertIn(contact.bio, response.content)
        self.assertIn(contact.email, response.content)
        self.assertIn(contact.jabber, response.content)
        self.assertIn(contact.other, response.content)
        self.assertIn(contact.skype, response.content)
        self.assertIn(contact.photo, response.content)