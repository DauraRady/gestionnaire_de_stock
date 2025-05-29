

from django.db import models
from django.conf import settings
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    en_stock = models.BooleanField(default=True)
    quantite = models.PositiveIntegerField(default=0)  # 🆕 champ stock

    def __str__(self):
        return self.nom
    
    
class Entreprise(models.Model):
    nom = models.CharField(max_length=255)
    identifiant = models.CharField(max_length=100, unique=True)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

class DemandeEntreprise(models.Model):
    nom = models.CharField(max_length=255)
    siret = models.CharField(max_length=14, unique=True)
    email_contact = models.EmailField()
    statut = models.CharField(
        max_length=20,
        choices=[('EN_ATTENTE', 'En attente'), ('ACCEPTEE', 'Acceptée'), ('REFUSEE', 'Refusée')],
        default='EN_ATTENTE'
    )
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.statut})"
class Mouvement(models.Model):
    TYPES = (
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
    )

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPES)
    quantite = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.type == 'ENTREE':
            self.produit.quantite += self.quantite
        elif self.type == 'SORTIE':
            if self.produit.quantite < self.quantite:
                raise ValueError("Pas assez de stock.")
            self.produit.quantite -= self.quantite
        self.produit.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} - {self.produit.nom} - {self.quantite}"