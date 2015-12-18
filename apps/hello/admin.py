from django.contrib import admin

from apps.hello.models import Contact, RequestLog, ObjectsDBLog
# Register your models here.


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'priority', 'method', 'path', 'remote_addr', 'time']
    list_filter = ['priority']
    list_editable = ['priority']

admin.site.register(Contact)
admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(ObjectsDBLog)
