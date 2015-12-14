from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from models import ObjectsDBLog


@receiver(post_save)
def log_objects_updated_added_event(sender, created, **kwargs):

    if created and sender.__name__ != 'ObjectsDBLog':
        ObjectsDBLog.objects.create(model=sender.__name__, action='created')

    if not created and sender.__name__ != 'ObjectsDBLog':
        ObjectsDBLog.objects.create(model=sender.__name__, action='updated')


@receiver(post_delete)
def log_objects_delete_event(sender, **kwargs):

    if sender.__name__ != 'ObjectsDBLog':
        ObjectsDBLog.objects.create(model=sender.__name__, action='deleted')
    return
