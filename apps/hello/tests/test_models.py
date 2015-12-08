from django.test import TestCase
from ..models import Contact, RequestLog

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
