from django.test import TestCase
from ..models import Contact, RequestLog, Team

# Create your tests here.


class ContactModelTests(TestCase):
    """Test all models
    """

    def test_unicode_contact(self):
        """Test unicode contact model
        """
        contact = Contact(name='John', surname='Snow')
        self.assertEqual(unicode(contact), u'John Snow')

    def test_unicode_requests(self):
        """Test unicode RequestsLog model
        """
        req = RequestLog(pk='1', method='GET', path='/requests/')
        self.assertEqual(unicode(req), u'1 GET /requests/')

    def test_unicode_team(self):
        """Test unicode Team model
        """
        team = Team(title='DjangoTeam', notes='5 developers')
        self.assertEqual(unicode(team), u'DjangoTeam')
