import json

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from apps.hello.models import Contact, RequestLog
from forms import ContactForm, TeamForm
import signals  # flake8: noqa00


def contact_data(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'contact_data.html', context)


def requests(request):
    request_log = RequestLog.objects.order_by('-time')
    order_by = request.GET.get('order_by', '')
    if order_by == 'priority':
        request_log = request_log.order_by(order_by)
    elif order_by == '-priority':
        request_log = request_log.order_by(order_by)
    return render(request, 'requests.html', {'request_log': request_log[:10]})


@login_required
def edit_form_contact(request, id):
    contacts = Contact.objects.get(pk=id)
    if request.POST and request.is_ajax():
        form = ContactForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            form.save_m2m()
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


@login_required
def create_team_form(request):
    if request.POST:
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            form.errors['success'] = 'Saved'
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form})
