from django import forms
from .models import Projet, Tache


class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'assigne_a', 'statut']