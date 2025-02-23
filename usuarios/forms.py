from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from  .models import Categoria_Producto 

class LoginForm(AuthenticationForm): 
    username = forms.CharField( 
        label='Usuario o Email', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario o email'}) 
    ) 
    password = forms.CharField( 
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}) 
    )

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria_Producto
        fields = ['nombre','descripcion']