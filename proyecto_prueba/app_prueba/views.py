from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoFormulario


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def agregar(request):
    vehiculo = Vehiculo()
    if request.method == 'POST':
        nuevoVehiculo = VehiculoFormulario(request.POST, instance=vehiculo)
        nuevoVehiculo.save()
        return render(request, 'index.html')
    else:
        formulario = VehiculoFormulario()
        return render(request, 'agregar.html', {'formulario': formulario})


def listar(request):
    vehiculo = Vehiculo.objects.all()
    return render(request, 'listar.html', {'vehiculo': vehiculo})
