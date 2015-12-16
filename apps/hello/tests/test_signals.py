from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.hello.models import ObjectsDBLog


@receiver(post_save)
def log_objects_updated_added_event(sender, created, **kwargs):

    if sender.__name__ == 'ObjectsDBLog':
        return

    action = 'created' if created else 'updated'
    ObjectsDBLog.objects.create(model=sender.__name__, action=action)


@receiver(post_delete)
def log_objects_delete_event(sender, **kwargs):

    if sender.__name__ == 'ObjectsDBLog':
        return

    ObjectsDBLog.objects.create(model=sender.__name__, action='deleted')