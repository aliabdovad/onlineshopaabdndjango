from django.shortcuts import render

# Create your views here.
from main.models import Customer


def home(request):
    customers = Customer.objects.all()
    return render(request, 'main/index.html', {'customers': customers})
