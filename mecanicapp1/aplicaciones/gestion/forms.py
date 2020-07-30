from django.forms import *
from .models import *

class SoloNombre(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb2'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        fields = '__all__'
        widgets = {
            'nombre' : TextInput(attrs={                
                'placeholder':'Nombre'}),            
        } 


class MarcaVehiculoForm(SoloNombre):    
    
    class Meta(SoloNombre.Meta):
        model = MarcaVehiculo   

