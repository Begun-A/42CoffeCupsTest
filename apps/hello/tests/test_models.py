from django.test import TestCase
from ..models import Contact

# Create your tests here.


class ContactModelTests(TestCase):
    """Test Contact model"""

    # Tests unicode method of Contact model
    def test_unicode(self):
        contact = Contact(name='John', surname='Snow')
        self.assertEqual(unicode(contact), u'John Snow')
