from django.conf import settings

def settigs_proc(request):
    return {'SETTINGS': settings}