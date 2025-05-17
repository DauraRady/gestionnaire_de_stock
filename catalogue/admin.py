from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'en_stock', 'lien_vers_site')

    def lien_vers_site(self, obj):
        url = reverse('liste_produits')  # le nom que tu as mis dans urls.py
        return format_html('<a href="{}" target="_blank">Voir sur le site</a>', url)

    lien_vers_site.short_description = 'Aperçu sur le site'

admin.site.register(Produit, ProduitAdmin)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'quantite', 'en_stock', 'lien_vers_site')
