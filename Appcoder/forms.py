from django import forms

class curso_formulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class estudiante_formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class profesor_formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class entregable_formulario(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()

""" class busquedaxcamada(forms.Form):
    camada = forms.IntegerField() """