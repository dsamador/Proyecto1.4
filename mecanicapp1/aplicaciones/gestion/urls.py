from django.urls import path
from .views import *



app_name = 'gestion'

urlpatterns = [        

    #********************************PATHS DE DATOS AUXILIARES***********************************

    path('list_marca/',               MarcaView.as_view(),             name = 'marcas'),
    
]