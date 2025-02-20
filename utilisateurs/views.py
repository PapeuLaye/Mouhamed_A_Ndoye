from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import InscriptionForm, ProfilForm


def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            print("✅ Utilisateur inscrit avec succès !")
            form.save()
            return redirect('connexion')
        else:
            print("❌ Erreurs :", form.errors)  # DEBUG pour voir les erreurs
    else:
        form = InscriptionForm()

    return render(request, 'utilisateurs/inscription.html', {'form': form})




def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_projets')
    return render(request, 'utilisateurs/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')


@login_required
def profil(request):
    if request.method == "POST":
        form = ProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProfilForm(instance=request.user)

    return render(request, 'utilisateurs/profil.html', {'form': form})
