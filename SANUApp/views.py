
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comentarios, Integrente, Servicios
from django.core.paginator import Paginator
from .forms import ComentariosForm

def inicio(request):
    return render(request, 'views/Inicio.html')

def nosotros(request):
    apinosotros = Integrente.objects.all()
    paginator = Paginator(apinosotros, 1) 

    pagina = request.GET.get("page") or 1
    
    nosotrosList = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, nosotrosList.paginator.num_pages +1)
    return render(request, 'views/Nosotros.html', {'nosotrosList': nosotrosList, 'paginas':paginas, 'pagina_actual':pagina_actual})

def servicios(request):
    apiservicios = Servicios.objects.all()
    paginator = Paginator(apiservicios, 3) 

    pagina = request.GET.get("page") or 1
    
    serviciosList = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, serviciosList.paginator.num_pages +1)
    return render(request, 'views/Servicios.html', {'serviciosList':serviciosList, 'paginas':paginas, 'pagina_actual':pagina_actual})

def contactanos(request):
    return render(request, 'views/Contactanos.html')

def comentarios(request):
    apicomentarios = Comentarios.objects.all()
    paginator = Paginator(apicomentarios, 3) 

    pagina = request.GET.get("page") or 1
    
    comentariosList = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, comentariosList.paginator.num_pages +1)
    return render(request, 'views/Comentarios.html', {'comentariosList':comentariosList, 'paginas':paginas, 'pagina_actual':pagina_actual})

def crearcomentarios(request):
    Formulario = ComentariosForm(request.POST or None, request.FILES or None)
    if Formulario.is_valid():
        Formulario.save()
        return redirect('comentarios')
    return render(request, 'views/CrearComentario.html', {'Formulario':Formulario})