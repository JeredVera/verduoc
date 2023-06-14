## VIEW  - URLS - HTML

from django.urls import path , include
from .views import *
from rest_framework import routers


# RUTAS DEL API
routers = routers.DefaultRouter()
routers.register('productos' , ProductoViewSet )

urlpatterns = [
    # API
    path('api/', include(routers.urls)),
    path('read_product_api/', read_product_api , name="read_product_api"),

    path('blank/', blank , name="blank"),
    path('checkout/', checkout , name="checkout"),
    path('', index , name="index"),
    path('product/', product , name="product"),
    path('store/', store , name="store"),
    path('login/', login , name="login"),
    path('suscribe/', suscribe , name="suscribe"),
    path('alimento/', alimento , name="alimento"),
    path('juguetes/', juguetes , name="juguetes"),
    path('ropa/', ropa , name="ropa"),
    path('cart/', cart , name="cart"),
    path('likes/', likes , name="likes"),

    #CRUD
    path('add_product/', add_product , name="add_product"),
    path('update_product/<id>/', update_product , name="update_product"),
    path('delete_product/<id>/', delete_product , name="delete_product"),
    path('read_product/', read_product , name="read_product"),


]