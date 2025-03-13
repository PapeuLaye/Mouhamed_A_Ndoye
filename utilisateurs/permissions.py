from rest_framework.permissions import BasePermission

class IsProfesseur(BasePermission):
    """
    Permission qui permet seulement aux professeurs d'effectuer certaines actions.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type_utilisateur == 'professeur'

class IsEtudiant(BasePermission):
    """
    Permission pour restreindre certaines actions aux étudiants.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type_utilisateur == 'etudiant'
