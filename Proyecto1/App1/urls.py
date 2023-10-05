from django.urls import path
from App1 import views

urlpatterns = [ path('', views.inicio, name="Inicio"),
                path('catalogo', views.catalogo, name="Catalogo"),
                path('cliente', views.cliente, name="Cliente"),
                path('proveedor', views.proveedor, name="Proveedor"),
                path('informacion', views.informacion, name="Informacion"),
                
                
                path('apiCatalogo', views.apiCatalogo, name="ApiCatalogo"),
                path('apiCliente', views.apiCliente, name="ApiCliente"),
                path('apiProveedor', views.apiProveedor, name="ApiProveedor"),
                
                path('buscarCatalogo', views.buscarCatalogo, name= "BuscarCatalogo" ),
]
