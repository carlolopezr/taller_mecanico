from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"taller_Serviexpress/home.html")

def listaServicios(request):
    return render(request,"taller_Serviexpress/listaServicios.html")