from django import forms
from .models import DemandeEntreprise

class DemandeEntrepriseForm(forms.ModelForm):
    class Meta:
        model = DemandeEntreprise
        fields = ['nom', 'siret', 'email_contact']
