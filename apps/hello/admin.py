from django.contrib import admin

from apps.hello.models import Contact, ObjectsDBLog
# Register your models here.
admin.site.register(Contact)
admin.site.register(ObjectsDBLog)
