from django import forms

from Conductor.views import conductor
from .models import TipoVehiculo, Vehiculo
from django.contrib.auth.models import Group

class FormularioVehiculo (forms.Form):
    placa = forms.CharField(max_length=7, label="Placa", widget=forms.TextInput(attrs={'class': 'form-control'}))
    marca = forms.CharField(max_length=50, label="Marca", widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.ModelChoiceField(queryset=TipoVehiculo.objects.all(), label="Tipo",widget=forms.Select(attrs={'class': 'form-select'}))
    conductor = forms.ModelChoiceField(queryset=Group.objects.get(name="CONDUCTOR").user_set.all(), label="Conductor",widget=forms.Select(attrs={'class': 'form-select'}))
    

class FormularioVehiculoEditar (forms.ModelForm):
    conductor = forms.ModelChoiceField(queryset=Group.objects.get(name="CONDUCTOR").user_set.all(), label="Conductor",widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Vehiculo
        fields = ['placa', 'marca', 'tipo', 'conductor']
        labels = {'placa': 'Placa', 'marca': 'Marca', 'tipo': 'Tipo', 'conductor': 'Conductor'}
        widgets = {'placa': forms.TextInput(attrs={'class': 'form-control'}),
                    'marca': forms.TextInput(attrs={'class': 'form-control'}),
                    'tipo': forms.Select(attrs={'class': 'form-control'}),
                    'conductor': forms.Select(attrs={'class': 'form-control'})}