# Create your views here.

from django.shortcuts import render

from apps.hello.models import Contact, RequestLog
# Create your views here.


def contact_data(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'contact_data.html', context)


def requests(request):
    request_log = RequestLog.objects.order_by('time').reverse()[:10]
    return render(request, 'requests.html', {'request_log': request_log})
