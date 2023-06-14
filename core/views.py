from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required #cada pagina que hay que verse loguiado se ingresa @login_required encima
from .models import *
from .forms import * 
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import viewsets
from .serializers import *
import requests

# SE ENCARGA DE MOSTRAR EN LA VISTA LOS DATOS
class ProductoViewSet(viewsets.ModelViewSet) :
    queryset = Producto.objects.all()
    #queryset = Producto.objects.filter(tipo=1)
    serializer_class = ProductoSerializer

# Create your views here.
## VIEW  - URLS - HTML

def blank(request):
    return render (request,'core/blank.html') 

def checkout(request):
    return render (request,'core/checkout.html') 

def index(request):
    ProductoAll = Producto.objects.all()
    data = {
        'Listado' : ProductoAll  
    }
    return render (request,'core/index.html' , data) 

@login_required
def product(request):
    return render (request,'core/product.html') 

@login_required
def store(request):
    return render (request,'core/store.html') 

def login(request):
    return render (request,'core/login.html') 

@login_required
def suscribe(request):
    return render (request,'core/suscribe.html')

@login_required
def alimento(request):
    ProductoAll = Producto.objects.all()
    data = {
        'Listado' : ProductoAll  
    }
    return render (request,'core/alimento.html' , data) 

@login_required
def juguetes(request):
    ProductoAll = Producto.objects.all()
    data = {
        'Listado' : ProductoAll  
    }
    return render (request,'core/juguetes.html' , data) 

@login_required
def ropa(request):
    ProductoAll = Producto.objects.all()
    data = {
        'Listado' : ProductoAll  
    }
    return render (request,'core/ropa.html' , data) 

@login_required
def cart(request):
    return render (request,'core/cart.html') 

@login_required
def likes(request):
    return render (request,'core/likes.html') 



# CRUD
@login_required
def add_product(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request , "Agregado Correctamente")
            return redirect(to="index")
        else :
            data["form"] = formulario

    return render (request,'core/add_product.html', data) 

@login_required
def update_product(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES) # RECIBE EL CONTENIDO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # INSERT
            messages.success(request , "Editado Correctamente")
            return redirect(to="index")
        else :
            data['form'] = formulario

    return render (request,'core/update_product.html', data)

@login_required
def delete_product(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="index")

@login_required
def read_product(request):
    ProductoAll = Producto.objects.all()
    page = request.GET.get('page', 1) 

    try:
        paginator = Paginator(ProductoAll , 5)
        ProductoAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity' : ProductoAll,
        'paginator' : paginator
    }

    return render(request,'core/read_product.html' , data)

# API
def read_product_api(request):
    # SOLICITUD DE API
    respuesta = requests.get('http://127.0.0.1:8000/api/productos/')
    respuesta2 = requests.get('https://mindicador.cl/api/')
    respuesta3 = requests.get('https://rickandmortyapi.com/api/character')
    
    # TRANSFORMAMOS EL JSON PARA LEERLO
    productos = respuesta.json()
    monedas = respuesta2.json()
    aux = respuesta3.json()
    personajes = aux['results']

    data = {
        'entity' : productos,
        'monedas' : monedas,
        'personajes' : personajes,
    }

    return render(request,'core/read_product_api.html' , data)