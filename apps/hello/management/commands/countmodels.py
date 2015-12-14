from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    """Test countmodels command, wich displays name model and number
    of objects in this model
    """
    help = "This command dislays all project models and the count of objects \
    in every model"

    def handle(self, *args, **options):
        for model in models.get_models():
            message = "Model: {0}, number of objects: {1}".format(
                model.__name__, model.objects.count())
            self.stdout.write(message)
            self.stderr.write('error:' + message)
