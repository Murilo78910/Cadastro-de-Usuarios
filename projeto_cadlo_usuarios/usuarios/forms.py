from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'email', 'senha']

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)


class EditarUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'email', 'senha']