from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    TYPE_CHOICES = (
        ('etudiant', 'Étudiant'),
        ('professeur', 'Professeur'),
    )
    type_utilisateur = models.CharField(max_length=10, choices=TYPE_CHOICES)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
