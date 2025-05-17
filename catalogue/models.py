

from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    en_stock = models.BooleanField(default=True)
    quantite = models.PositiveIntegerField(default=0)  # 🆕 champ stock

    def __str__(self):
        return self.nom