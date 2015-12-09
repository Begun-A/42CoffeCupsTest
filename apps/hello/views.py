# Create your views here.
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from apps.hello.models import Contact, RequestLog
from forms import ContactForm
# Create your views here.


def contact_data(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'contact_data.html', context)


def requests(request):
    request_log = RequestLog.objects.order_by('time').reverse()[:10]
    return render(request, 'requests.html', {'request_log': request_log})


def edit_form_contact(request, id):
    contacts = Contact.objects.get(pk=id)
    if request.POST:
        form = ContactForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            if request.is_ajax():
                return HttpResponse('OK')
        else:
            if request.is_ajax():
                errors_dict = {}
                if form.errors:
                    for e in form.errors:
                        error = form.errors[e]
                        errors_dict[e] = unicode(error)

                return HttpResponseBadRequest(json.dumps(errors_dict))
    else:
        form = ContactForm(instance=contacts)

    return render(request, 'edit_form.html', {'form': form})
