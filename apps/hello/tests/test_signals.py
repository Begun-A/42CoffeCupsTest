from django.test import TestCase

from apps.hello.models import Contact, ObjectsDBLog


class ObjectsDBLogTest(TestCase):
    """Tests for signals
    """
    fixtures = ['hello_fixture.json']

    def test_object_create(self):
        """Test signal, when objects created
        """
        ObjectsDBLog.objects.all().delete()
        self.assertEqual(ObjectsDBLog.objects.all().count(), 0)
        Contact.objects.create(name='John',
                               surname='Snow',
                               birth_date='1992-12-01',
                               email='snow.j@gmail.com',
                               skype='j-snow',
                               jabber='snow@khavr.com',
                               other='Winterfell',
                               bio='John Snow fights with white walker')
        self.assertEqual(Contact.objects.all().count(), 2)
        self.assertEqual(ObjectsDBLog.objects.all().count(), 1)
        self.assertEqual(ObjectsDBLog.objects.get(pk=1).action, 'created')

    def test_object_update(self):
        """Test signal, when objects updated
        """
        ObjectsDBLog.objects.all().delete()
        contact = Contact.objects.get(pk=1)
        self.assertEqual(contact.name, 'Oleksandr')
        contact.name = 'Mike'
        contact.save()
        contact = Contact.objects.get(pk=1)
        self.assertEqual(contact.name, 'Mike')
        self.assertEqual(ObjectsDBLog.objects.all().count(), 1)
        self.assertEqual(ObjectsDBLog.objects.get(pk=1).action, 'updated')

    def test_object_delete(self):
        """Test signal, when objects deleted
        """
        ObjectsDBLog.objects.all().delete()
        self.assertEqual(Contact.objects.all().count(), 1)
        Contact.objects.all().delete()
        self.assertEqual(ObjectsDBLog.objects.all().count(), 1)
        self.assertEqual(ObjectsDBLog.objects.get(pk=1).action, 'deleted')
