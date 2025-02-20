from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projet, Tache
from .forms import ProjetForm, TacheForm


@login_required
def liste_projets(request):
    projets = Projet.objects.filter(chef_projet=request.user)
    return render(request, 'projets/liste_projets.html', {'projets': projets})

@login_required
def creer_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.chef_projet = request.user
            projet.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm()
    return render(request, 'projets/creer_projet.html', {'form': form})

@login_required
def modifier_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id, chef_projet=request.user)
    if request.method == "POST":
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'projets/modifier_projet.html', {'form': form})

@login_required
def supprimer_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id, chef_projet=request.user)
    if request.method == "POST":
        projet.delete()
        return redirect('liste_projets')
    return render(request, 'projets/supprimer_projet.html', {'projet': projet})



@login_required
def ajouter_tache(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id, chef_projet=request.user)
    if request.method == "POST":
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.projet = projet
            tache.save()
            return redirect('detail_projet', projet_id=projet.id)
    else:
        form = TacheForm()
    return render(request, 'projets/ajouter_tache.html', {'form': form, 'projet': projet})

@login_required
def modifier_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id, projet__chef_projet=request.user)
    if request.method == "POST":
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('detail_projet', projet_id=tache.projet.id)
    else:
        form = TacheForm(instance=tache)
    return render(request, 'projets/modifier_tache.html', {'form': form})

@login_required
def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id, projet__chef_projet=request.user)
    projet_id = tache.projet.id
    if request.method == "POST":
        tache.delete()
        return redirect('detail_projet', projet_id=projet_id)
    return render(request, 'projets/supprimer_tache.html', {'tache': tache})

@login_required
def detail_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id, chef_projet=request.user)
    taches = projet.taches.all()
    return render(request, 'projets/detail_projet.html', {'projet': projet, 'taches': taches})
