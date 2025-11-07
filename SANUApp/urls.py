from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('servicios', views.servicios, name='servicios'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('comentarios', views.comentarios, name='comentarios'),
    path('crearcomentarios', views.crearcomentarios, name='crearcomentarios'),  
] 
