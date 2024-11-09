from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def crear(request):
    return render(request, 'crear.html')