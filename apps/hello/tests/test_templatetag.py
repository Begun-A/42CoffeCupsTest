from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class TemlateTagTest(TestCase):
    """Tests temlplate tags
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_edit_link_tag(self):
        """Test template tag {% edit_link object %}
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.url)
        self.assertContains(response,
                            '<a href="/admin/hello/contact/1/">(admin)</a>', 1)
