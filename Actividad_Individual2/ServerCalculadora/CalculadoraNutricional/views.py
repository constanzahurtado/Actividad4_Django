from django.shortcuts import redirect, render
from .models import Usuario
from .forms import RegistroForm

# Create your views here.

def index(request):
    return render(request, 'CalculadoraNutricional/index.html')

def usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, 'CalculadoraNutricional/usuarios.html',{'data': usuario})

def registro(request):
    if request.method == "POST":
        form = RegistroForm(data = request.POST)
        if form.is_valid():
            proveedor = form.save(commit = False)
            proveedor.save()
        return redirect('/usuarios')
    else:
        form = RegistroForm()
        return render(request,'CalculadoraNutricional/registro_usuario.html', {"form": form})