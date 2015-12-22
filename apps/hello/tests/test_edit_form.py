import json

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Contact, Team


class FormEditTest(TestCase):
    """Tests form which edit contact data.
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()
        self.url = reverse('edit_form', kwargs={'id': 1})

    def test_access_edit_form(self):
        """Check access edit form
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_form_page(self):
        """Check data on the form page"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        contact = Contact.objects.get(pk=1)
        self.assertContains(response, contact.name, 1)
        self.assertContains(response, contact.birth_date, 1)
        self.assertContains(response, contact.email, 1)
        self.assertContains(response, contact.skype, 1)

    def test_edit_form_post_valid_data(self):
        """Test edit form post with valid data
        """
        response = self.client.post(self.url, {'name': 'Mike'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        team1 = Team(title='Team1')
        team1.save()
        response = self.client.post(self.url, {'name': 'Mike',
                                               'email': 'a.mike@live.com',
                                               'birth_date': '2000-12-31',
                                               'jabber': 'begun-m@khavr.com',
                                               'contact_team': [team1.pk]},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'Mike')
        self.assertEqual(contact.email, 'a.mike@live.com')
        self.assertEqual(contact.birth_date.isoformat(), '2000-12-31')
        self.assertEqual(contact.jabber, 'begun-m@khavr.com')
        self.assertEqual(list(contact.contact_team.all()), [team1])

    def test_edit_form_post_not_valid_data(self):
        """Test edit form post with not valid data
        """
        response = self.client.post(self.url, {'name': 'Mike'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.url, {'name': '',
                                               'email': '',
                                               'birth_date': '',
                                               'jabber': ''},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        for key in content.keys():
            self.assertIn(u'This field is required.', content[key])

        response = self.client.post(self.url, {'birth_date': '2000-1231'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertIn(u'Enter a valid date.', content['birth_date'])
