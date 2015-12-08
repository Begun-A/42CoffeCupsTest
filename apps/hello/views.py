from django.shortcuts import render

from apps.hello.models import Contact


def contact_data(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'contact_data.html', context)


def requests(request):
    return render(request, 'requests.html', {})
