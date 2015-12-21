from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..models import Team
from ..forms import TeamForm


class FormEditTest(TestCase):
    """Tests form which edit contact data.
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()
        self.url = reverse('add_team')

    def test_access_edit_form(self):
        """Check access add team form
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_form_page(self):
        """Check data on the add team form page"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        form = TeamForm()
        self.assertContains(response, form['title'], 1)
        self.assertContains(response, form['notes'], 1)

    def test_add_team_form_post_valid_data(self):
        """Test add team form post with valid data
        """
        response = self.client.post(self.url, {'title': 'TestTeam'})
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.url, {'title': 'TestTeam',
                                               'notes': '5 developers'})
        self.assertEqual(response.status_code, 200)
        team = Team.objects.first()
        self.assertEqual(team.title, 'TestTeam')
        self.assertEqual(team.notes, '5 developers')

    def test_add_team_form_post_not_valid_data(self):
        """Test add team form post with not valid data
        """
        response = self.client.post(self.url, {'title': 'TestTeam'}, )
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        response = self.client.post(self.url, {'title': '',
                                               'notes': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'This field is required.', 1)
