import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from apps.hello.models import Contact, RequestLog
from forms import ContactForm


def contact_data(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'contact_data.html', context)


def requests(request):
    request_log = RequestLog.objects.order_by('time').reverse()[:10]
    return render(request, 'requests.html', {'request_log': request_log})


@login_required
def edit_form_contact(request, id):
    contacts = Contact.objects.get(pk=id)
    if request.POST and request.is_ajax():
        form = ContactForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return HttpResponse('OK')
        else:
            errors_dict = {}
            for e in form.errors:
                error = form.errors[e]
                errors_dict[e] = unicode(error)
            return HttpResponseBadRequest(json.dumps(errors_dict))
    else:
        form = ContactForm(instance=contacts)

    return render(request, 'edit_form.html', {'form': form})
