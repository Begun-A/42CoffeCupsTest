from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from apps.hello.models import Contact
# Create your views here.

def contact_data(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'contact_data.html', context)

def requests(request):

    return render(request, 'requests.html', {})