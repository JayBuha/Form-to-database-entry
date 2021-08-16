from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')


def contect(request):
    if request.method == "POST":
        first_name = request.POST.get('F_name')
        last_name = request.POST.get('L_name')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        
        A = Contact(First_name=first_name, Last_name=last_name, Email=email, password=password, date=datetime.today())
        A.save()
        messages.success(request, 'You are success fully ragistreted!!.')

    return render(request,'contect.html')
