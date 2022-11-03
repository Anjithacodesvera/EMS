from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'log/login.html')

def index(request):
    return render(request, 'log/index1.html')

def employee(request):
    return render(request, 'log/index2.html')

def add(request):
    return render(request, 'log/add.html')