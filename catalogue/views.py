from django.shortcuts import render, redirect
from .models import Produit  
from .forms import DemandeEntrepriseForm
from django.contrib import messages

def liste_produits(request):
    produits = Produit.objects.all()  # je prends tous les produits
    return render(request, 'catalogue/liste.html', {'produits': produits})


def accueil(request):
    return render(request, 'catalogue/accueil.html')

def demande_entreprise(request):
    if request.method == 'POST':
        form = DemandeEntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre demande a été envoyée avec succès.")
            return redirect('accueil')
    else:
        form = DemandeEntrepriseForm()
    return render(request, 'catalogue/demande_entreprise.html', {'form': form})