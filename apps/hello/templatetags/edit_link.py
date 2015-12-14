from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(object):
    """Template tag {% edit_link object %}
    """
    content_type = ContentType.objects.get_for_model(object.__class__)
    return reverse(
        "admin:%s_%s_change" % (content_type.app_label, content_type.model),
        args=(object.id,))
