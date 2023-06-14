from django.contrib import admin
from .models import TipoProducto , Producto
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio" , "stock" , "tipo"]
    list_editable = ["precio" , "stock" , "tipo"]
    search_fields = ["nombre"]
    list_filter = ['tipo']
    list_per_page = 10
    
admin.site.register(TipoProducto)
admin.site.register(Producto , ProductosAdmin)