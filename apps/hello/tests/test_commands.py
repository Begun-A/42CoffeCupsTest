from StringIO import StringIO

from django.test import TestCase
from django.core.management import call_command


class CommandsTests(TestCase):
    """Tests commands hello app
    """

    def test_countmodels_command(self):
        """Test countmodels command.
        """
        out = StringIO()
        err = StringIO()
        call_command('countmodels', stderr=err, stdout=out)

        self.assertIn('Model: Contact, number of objects:', out.getvalue())
        self.assertIn('error:Model: MigrationHistory, number of objects:',
                      err.getvalue())
