from django import forms
from .models import TipoServicio, TipoIdentificacion, FormaPago, Municipio, EnvioGuia
# from Cotizaciones.models import Municipio

class FormularioRemitente(forms.Form):
    servicio = forms.ModelChoiceField(queryset=TipoServicio.objects.all(),widget=forms.Select(attrs={'class': 'form-select'})) # aqui seleccionamos el tipo de servicio si es documentos o paquetes         
    # numeroguia = forms.CharField(max_length=50, label='Número de Guía')
    tipoIdRemitente = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=TipoIdentificacion.objects.all(), label = 'Tipo de Identificación')
    identificacionRemi = forms.CharField(label='Identificación', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombreRemi = forms.CharField(label='Nombre', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ciudadRemi = forms.ModelChoiceField(queryset=Municipio.objects.all(), label = 'Ciudad',widget=forms.Select(attrs={'class': 'form-control'}))
    direccionRemi = forms.CharField(label='Dirección', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefonoRemi = forms.CharField(label='Teléfono', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correoRemi = forms.CharField(label='Correo', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    
class FormularioRemitente2(forms.ModelForm):
    class Meta:
        model = EnvioGuia
        fields = ('tipoServicio', 'numueroguia', 'tipoIdRemitente', 'identificacionRemi', 'nombreRemi', 'ciudadRemi', 'direccionRemi', 'telefonoRemi', 'correoRemi')
        labels = { 'tipoServicio': 'Servicio', 'numueroguia': 'Número de Guía', 'tipoIdRemitente': 'Tipo de Identificación', 'identificacionRemi': 'Identificación', 'nombreRemi': 'Nombre', 'ciudadRemi': 'Ciudad', 'direccionRemi': 'Dirección', 'telefonoRemi': 'Teléfono', 'correoRemi': 'Correo'}
        widgets = { 'tipoServicio': forms.Select(attrs={'class': 'form-control'}), 
        'numueroguia': forms.TextInput(attrs={'class': 'form-control'}), 
        'tipoIdRemitente': forms.Select(attrs={'class': 'form-control'}), 
        'identificacionRemi': forms.TextInput(attrs={'class': 'form-control'}), 
        'nombreRemi': forms.TextInput(attrs={'class': 'form-control'}), 
        'ciudadRemi': forms.Select(attrs={'class': 'form-control'}), 
        'direccionRemi': forms.TextInput(attrs={'class': 'form-control'}), 
        'telefonoRemi': forms.TextInput(attrs={'class': 'form-control'}), 
        'correoRemi': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super(FormularioRemitente2, self).__init__(*args, **kwargs)
        self.fields['tipoServicio'].disabled = True
        self.fields['numueroguia'].disabled = True
        self.fields['tipoIdRemitente'].disabled = True
        self.fields['identificacionRemi'].disabled = True
        self.fields['nombreRemi'].disabled = True
        self.fields['ciudadRemi'].disabled = True
        self.fields['direccionRemi'].disabled = True
        self.fields['telefonoRemi'].disabled = True
        self.fields['correoRemi'].disabled = True

class FormularioDestinatario(forms.Form):
    tipoIdDestinatario = forms.ModelChoiceField(queryset=TipoIdentificacion.objects.all(), label = 'Tipo de Identificación',widget=forms.Select(attrs={'class': 'form-select'}))
    identificacionDesti = forms.CharField(label='Identificación', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombreDesti = forms.CharField(label='Nombre', max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ciudadDesti = forms.ModelChoiceField(queryset=Municipio.objects.all(), label = 'Ciudad',widget=forms.Select(attrs={'class': 'form-select'}))
    direccionDesti = forms.CharField(label='Dirección', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefonoDesti = forms.CharField(label='Teléfono', max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    correoDesti = forms.CharField(label='Correo', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

class FormularioDestinatario2(forms.ModelForm):
    class Meta:
        model = EnvioGuia
        fields = ('tipoIdDesti', 'identificacionDesti', 'nombreDesti', 'ciudadDesti', 'direccionDesti', 'telefonoDesti', 'correoDesti')
        labels = { 'tipoIdDesti': 'Tipo de Identificación', 'identificacionDesti': 'Identificación', 'nombreDesti': 'Nombre', 'ciudadDesti': 'Ciudad', 'direccionDesti': 'Dirección', 'telefonoDesti': 'Teléfono', 'correoDesti': 'Correo'}
        widgets = { 'tipoIdDesti': forms.Select(attrs={'class': 'form-control'}), 
        'identificacionDesti': forms.TextInput(attrs={'class': 'form-control'}), 
        'nombreDesti': forms.TextInput(attrs={'class': 'form-control'}), 
        'ciudadDesti': forms.Select(attrs={'class': 'form-control'}), 
        'direccionDesti': forms.TextInput(attrs={'class': 'form-control'}), 
        'telefonoDesti': forms.TextInput(attrs={'class': 'form-control'}), 
        'correoDesti': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super(FormularioDestinatario2, self).__init__(*args, **kwargs)
        self.fields['tipoIdDesti'].disabled = True
        self.fields['identificacionDesti'].disabled = True
        self.fields['nombreDesti'].disabled = True
        self.fields['ciudadDesti'].disabled = True
        self.fields['direccionDesti'].disabled = True
        self.fields['telefonoDesti'].disabled = True
        self.fields['correoDesti'].disabled = True

class FormularioUnidades(forms.Form):
    peso = forms.IntegerField(label='Peso (kg)', required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    largo = forms.CharField(label='Largo (cm)', max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ancho = forms.CharField(label='Ancho (cm)', max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    alto = forms.CharField(label='Alto (cm)', max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    contiene = forms.CharField(label='Contiene', max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    forma = forms.ModelChoiceField(queryset=FormaPago.objects.all(), label='Forma de Pago',widget=forms.Select(attrs={'class': 'form-select'}))


class FormularioUnidades2(forms.ModelForm):
    class Meta:
        model = EnvioGuia
        fields = ['formapagp', 'peso', 'largo', 'ancho', 'alto', 'contiene', 'valor']
        labels = { 'formapagp': 'Forma de Pago', 'peso': 'Peso Real', 'largo': 'Largo', 'ancho': 'Ancho', 'alto': 'Alto', 'contiene': 'Contiene', 'valor': 'Valor'}
        widgets = { 'formapagp': forms.Select(attrs={'class': 'form-control'}), 
        'peso': forms.TextInput(attrs={'class': 'form-control'}), 
        'largo': forms.TextInput(attrs={'class': 'form-control'}), 
        'ancho': forms.TextInput(attrs={'class': 'form-control'}), 
        'alto': forms.TextInput(attrs={'class': 'form-control'}), 
        'contiene': forms.TextInput(attrs={'class': 'form-control'}), 
        'valor': forms.TextInput(attrs={'class': 'form-control'})}

