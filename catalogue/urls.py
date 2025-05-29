from django.urls import path
from .views import liste_produits, accueil, demande_entreprise

urlpatterns = [
    path('', accueil, name='accueil'),  # page d'accueil
    path('produits/', liste_produits, name='liste_produits'),  # liste des produits
    path('demande-entreprise/', demande_entreprise, name='demande_entreprise'),  # formulaire entreprise
]
