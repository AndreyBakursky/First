from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['1111-2222-3333-4444', 'test@gmail.com']})
