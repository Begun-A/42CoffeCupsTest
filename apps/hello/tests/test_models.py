from django.test import TestCase
from ..models import Contact

# Create your tests here.


class ContactModelTests(TestCase):
    """Test Contact model
    """
    def test_unicode(self):
        """Test unicode Contact model
        """
        contact = Contact(name='Jon', surname='Snow')
        self.assertEqual(unicode(contact), u'Jon Snow')
