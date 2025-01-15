from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def presta(request):
    return render(request,"presta.html")

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
