from django.contrib import admin
from django.urls import path, include
from PosGre.views import cliente_lista, area_lista, empleado_lista, venta_lista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("PosGre.urls")),
    path('',cliente_lista, name='cliente_list' ),
    path('',area_lista, name='area_list'),
    path('',empleado_lista, name='empleado_list'),
    path('',venta_lista, name='venta_list'),
]
