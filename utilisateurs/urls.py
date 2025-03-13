from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import inscription, connexion, deconnexion, profil, InscriptionAPIView, api_profil

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('profil/', profil, name='profil'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', InscriptionAPIView.as_view(), name='api_register'),
    path('api/profil/', api_profil, name='api_profil'),  # ✅ Nouveau endpoint API pour voir son profil
]
