from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    type_utilisateur = forms.ChoiceField(choices=Utilisateur.TYPE_CHOICES, label="Type d'utilisateur")

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'type_utilisateur', 'password1', 'password2']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'type_utilisateur', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'type_utilisateur': forms.Select(attrs={'class': 'form-select'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }