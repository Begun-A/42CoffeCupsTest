from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Contact


class TestContactData(TestCase):
    """Tests contact_data view
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

    def test_more_then_one_entry_in_db(self):
        """Test contact view, when more then one entry in db
        """
        Contact.objects.create(name='Jon',
                               surname='Snow',
                               birth_date='1992-12-01',
                               email='snow.j@gmail.com',
                               skype='j-snow',
                               jabber='snow@khavr.com',
                               other='Winterfell',
                               bio='Jon Snow fights with white walker')
        contacts = Contact.objects.all()
        self.assertEqual(Contact.objects.count(), 2)
        response = self.client.get(self.url)
        self.assertNotEqual(contacts[1], response.context['contact'])
        self.assertEqual(contacts[0], response.context['contact'])

    def test_no_data_in_db(self):
        """Test contact view, when no data in db
        """
        Contact.objects.all().delete()
        contacts = Contact.objects.first()
        self.assertEqual(Contact.objects.count(), 0)
        response = self.client.get(self.url)
        self.assertEqual(contacts, None)
        self.assertEqual(contacts, response.context['contact'])
