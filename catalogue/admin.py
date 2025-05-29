from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Entreprise, Produit, Mouvement, DemandeEntreprise

# Produit
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'quantite', 'en_stock', 'lien_vers_site')

    def lien_vers_site(self, obj):
        url = reverse('liste_produits')  # à condition que tu aies bien cette vue dans urls.py
        return format_html('<a href="{}" target="_blank">Voir sur le site</a>', url)

    lien_vers_site.short_description = 'Aperçu sur le site'

# Entreprise
@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'date_creation')
    search_fields = ('nom', 'identifiant')

# Mouvement
@admin.register(Mouvement)
class MouvementAdmin(admin.ModelAdmin):
    list_display = ('produit', 'type', 'quantite', 'date', 'utilisateur')
    list_filter = ('type', 'date')
    search_fields = ('produit__nom', 'utilisateur__username')

# Demande d'inscription
@admin.register(DemandeEntreprise)
class DemandeEntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'siret', 'email_contact', 'statut', 'date_demande')
    list_filter = ('statut',)
    search_fields = ('nom', 'siret', 'email_contact')
    actions = ['accepter_demandes', 'refuser_demandes']

    def accepter_demandes(self, request, queryset):
        queryset.update(statut='ACCEPTEE')
        self.message_user(request, f"{queryset.count()} demande(s) acceptée(s).")

    def refuser_demandes(self, request, queryset):
        queryset.update(statut='REFUSEE')
        self.message_user(request, f"{queryset.count()} demande(s) refusée(s).")
