from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Contact, Team


class TestContactData(TestCase):
    """Tests contact page
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        # remember url
        self.url = reverse('contact')
        # remember test browser
        self.client = Client()

    def test_fixtures(self):
        """Test, if db has more then one enter
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
        t1 = Team(title='team1')
        t2 = Team(title='team2')
        t1.save()
        t2.save()
        contact = Contact(name='John',
                          surname='Snow',
                          birth_date='1992-12-01',
                          email='snow.j@gmail.com',
                          skype='j-snow',
                          jabber='snow@khavr.com',
                          other='Winterfell',
                          bio='John Snow fights with white walker')
        contact.save()
        contact.contact_team.add(t2)
        contacts = Contact.objects.all()
        contacts[0].contact_team.add(t1)
        self.assertEqual(Contact.objects.count(), 2)
        response = self.client.get(self.url)
        self.assertEqual(contacts[0], response.context['contact'])
        self.assertContains(response, 'Skype:', 1)
        self.assertContains(response, t1.title, 1)
        self.assertNotEqual(contacts[1], response.context['contact'])
        self.assertNotContains(response, 'John')
        self.assertNotContains(response, t2.title)

    def test_no_data_in_db(self):
        """Test contact view, when no data in db
        """
        Contact.objects.all().delete()
        contacts = Contact.objects.first()
        self.assertEqual(Contact.objects.count(), 0)
        response = self.client.get(self.url)
        self.assertEqual(contacts, None)
        self.assertEqual(contacts, response.context['contact'])

    def test_links(self):
        """Test edit_form, requests, login, logout link on the contact page
        """
        contact = Contact.objects.first()

        response = self.client.get(self.url)
        self.assertContains(response, reverse('login'), 1)

        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.assertContains(response,
                            reverse('edit_form', kwargs={'id': contact.id}), 1)
        self.assertContains(response, reverse('requests'), 1)
        self.assertContains(response, reverse('logout'), 1)

        self.client.logout()
        response = self.client.get(self.url)
        self.assertContains(response, reverse('login'), 1)

    def test_temlate_login(self):
        """Test temlate login elenets
        """
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'name="username"', 1)
        self.assertContains(response, 'name="password"', 1)
        self.assertContains(response, 'type="submit"', 1)
