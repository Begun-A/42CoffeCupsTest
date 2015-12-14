from django.conf import settings


def settings_proc(request):
    return {'SETTINGS': settings}
