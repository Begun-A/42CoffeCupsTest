from django.test import TestCase,Client
from django.core.urlresolvers import reverse

from ..models import Contact

class FormEditTest(TestCase):
    """Tests form which edit contact data.
    """
    fixtures = ['hello_fixture.json']

    def setUp(self):
        self.client = Client()
        self.url = reverse('form_edit', kwargs={'pk':1})

    def test_access_edit_form(self):
        """Check access edit form
        """
        response= self.client.get(self.url)
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
        self.assertContains(response, contact.surname, 1)
        self.assertContains(response, contact.birth_date, 1)
        self.assertContains(response, contact.email, 1)
        self.assertContains(response, contact.skype, 1)
        self.assertContains(response, contact.jabber, 1)
        self.assertContains(response, contact.other, 1)
        self.assertContains(response, contact.bio, 1)

    def test_edit_form_post(self):
        """Test edit form post on validation and required fields"""
        self.client.login(username='admin', password='admin')

        response = self.client.post(self.url, {'date': '2000-1231'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form']['date'].errors, [u'The data is not valid.'])

        response = self.client.post(self.url, {'name': '', 'email':''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form']['name'].errors, [u'This field is required.'])
        self.assertEqual(response.context['form']['email'].errors, [u'This field is required.'])

