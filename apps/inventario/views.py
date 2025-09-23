from django.shortcuts import render


# Create your views here.


def login(request):
    return render(request, "core/login.html")

def dashboard(request):
    return render(request, "inventario/dashboard.html")
