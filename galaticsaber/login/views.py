from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')