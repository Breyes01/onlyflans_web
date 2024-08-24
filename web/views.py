from django.shortcuts import render
from django.http import HttpResponse
from flan.models import Flan, ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #este comando trae todos los objetos flanes
    #flans = Flan.objects.all()
    flans = Flan.objects.filter(is_private=False) #estos son los flanes publicos
    context = {'flans':flans}
    return render(request, 'web/index.html', context)

def about(request):
    return render(request, 'web/about.html')


@login_required
def welcome(request):
    flans = Flan.objects.filter(is_private=True) #estos son los flanes privados
    context = {'flans':flans}
    return render(request, 'web/welcome.html', context)


def contact(request):
    if request.method == 'POST':
        customer_email = request.POST.get('customer_email')
        customer_name = request.POST.get('customer_name')
        message = request.POST.get('message')
        contact = ContactForm(customer_email=customer_email, customer_name=customer_name, message=message)
        contact.save()
        return render(request, 'web/contact_success.html')
    
    return render(request, 'web/contact.html')

def list_contact(request):
    contacts = ContactForm.objects.all()
    context = {'contacts': contacts}
    return render(request, 'web/list_contact.html', context)

def delivery(request):
    return render(request, 'web/delivery.html')