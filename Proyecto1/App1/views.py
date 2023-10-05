from django.shortcuts import render
from App1.forms import *
from django.http import HttpResponse
from App1.models import *



def inicio(request): #vista para inicio
    return render(request,'App1/inicio.html')

def catalogo(request):#vista para catalogo
    return render(request,'App1/catalogo.html')

def cliente(request):#vista para cliente
    return render(request,'App1/cliente.html')

def proveedor(request): #vista para proveedor
    return render(request,'App1/proveedor.html')

def informacion(request): #vista para informacion
    return render(request,'App1/informacion.html')
 
def apiCatalogo(request):   #funcion para formulario catalogo
 
      if request.method == "POST":
 
            miFormulario = CatalogoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  catalogo = Catalogo(marca=informacion["marca"], modelo=informacion["modelo"],valor=informacion["valor"] )
                  catalogo.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = CatalogoFormulario()
 
      return render(request, "App1/apiCatalogo.html", {"miFormulario": miFormulario})

def apiCliente(request):  #funcion para formulario cliente
 
      if request.method == "POST":
 
            miFormulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"], edad =informacion["edad"] )
                  cliente.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = ClienteFormulario()
 
      return render(request, "App1/apiCliente.html", {"miFormulario": miFormulario})

def apiProveedor(request): #funcion para formulario proveedor
 
      if request.method == "POST":
 
            miFormulario = ProveedorFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  proveedor = Proveedor(nombre=informacion["nombre"], direccion=informacion["direccion"],email=informacion["email"], telefono=informacion["telefono"] )
                  proveedor.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = ProveedorFormulario()
 
      return render(request, "App1/apiProveedor.html", {"miFormulario": miFormulario})

def buscarCatalogo(request): #funcion para buscar en el catalogo
 
      if request.method == "POST":
 
            miFormulario = BuscarCatalogo(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  marcas = Catalogo.objects.filter(marca__icontains=informacion["marca"])                
                  return render(request, "App1/buscarCatalogo.html", {"marcas" : marcas})
      else:
            miFormulario = BuscarCatalogo()
 
      return render(request, "App1/apiCatalogo.html", {"miFormulario": miFormulario})