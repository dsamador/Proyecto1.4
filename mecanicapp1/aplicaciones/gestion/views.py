from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count
from django.forms import model_to_dict
import json
from .models import *
from .forms import *
from datetime import datetime
from django.http import JsonResponse


class MarcaView(LoginRequiredMixin, TemplateView):    
    template_name = 'auxdata/marca/list_marca.html'    
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:                         
            action = request.POST['action']                      
            if action == 'searchdata':
                print('Buscando los datos')
                data = []
                for i in MarcaVehiculo.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                m = MarcaVehiculo()
                m.nombre = request.POST['nombre']
                m.save()
            elif action == 'edit':
                m = MarcaVehiculo.objects.get(pk=request.POST['id'])
                m.nombre = request.POST['nombre']                
                m.save()
            elif action == 'delete':
                m = MarcaVehiculo.objects.get(pk=request.POST['id'])
                m.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe = False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de marcas'                
        context['entity'] = 'Marcas'
        context['form'] = MarcaVehiculoForm()
        context['desc'] = 'Marcas'   
        return context