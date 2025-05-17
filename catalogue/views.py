from django.shortcuts import render
from .models import Produit  
def liste_produits(request):
    produits = Produit.objects.all()  # je prends tous les produits
    return render(request, 'catalogue/liste.html', {'produits': produits})



