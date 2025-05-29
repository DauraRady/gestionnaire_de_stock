from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

class UtilisateurAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Rôle & Entreprise", {'fields': ('role', 'entreprises', 'actif')}),
    )

admin.site.register(Utilisateur, UtilisateurAdmin)
