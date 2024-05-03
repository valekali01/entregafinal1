from django import forms
from django.contrib.auth.models import User
from .models import Avatar, Sala

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class SalaSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de la sala"
    )
    disponible = forms.BooleanField(required=False, label="Sólo salas disponibles")
    capacidad_minima = forms.IntegerField(required=False, label="Salas con capacidad mayor a:")
    tipo_de_sala = forms.ChoiceField(choices=Sala.Tipo.choices)


class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput, help_text='Introduzca la misma contraseña que antes, para su verificación.')

    error_messages = {
        'password_mismatch': "Las dos contraseñas no coinciden.",
        'password_too_short': "Esta contraseña es demasiado corta. Debe contener al menos %(min_length)d caracteres.",
        'password_common': "Esta contraseña es demasiado común.",
        'password_entirely_numeric': "Esta contraseña es enteramente numérica.",
    }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        from django import forms
from .models import Sala, Reserva

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'



