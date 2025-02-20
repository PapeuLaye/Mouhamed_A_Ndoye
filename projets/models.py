from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Récupère le modèle utilisateur de Django
Utilisateur = get_user_model()

class Projet(models.Model):
    """Modèle représentant un projet"""
    nom = models.CharField(max_length=200)  # Nom du projet
    description = models.TextField(blank=True)  # Description facultative
    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création automatique
    chef_projet = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="projets")

    def __str__(self):
        return self.nom  # Retourne le nom du projet dans l'administration

class Tache(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="taches")
    assigne_a = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')

    def __str__(self):
        return f"{self.titre} - {self.get_statut_display()}"
