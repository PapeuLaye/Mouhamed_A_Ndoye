from django.urls import path
from .views import liste_projets, creer_projet, modifier_projet, supprimer_projet, ajouter_tache, modifier_tache, \
    supprimer_tache, detail_projet

urlpatterns = [
    path('', liste_projets, name='liste_projets'),
    path('creer/', creer_projet, name='creer_projet'),
    path('modifier/<int:projet_id>/', modifier_projet, name='modifier_projet'),
    path('supprimer/<int:projet_id>/', supprimer_projet, name='supprimer_projet'),
    path('<int:projet_id>/ajouter_tache/', ajouter_tache, name='ajouter_tache'),
    path('tache/<int:tache_id>/modifier/', modifier_tache, name='modifier_tache'),
    path('tache/<int:tache_id>/supprimer/', supprimer_tache, name='supprimer_tache'),
    path('<int:projet_id>/', detail_projet, name='detail_projet'),

]
