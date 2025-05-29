from django.contrib.auth.models import AbstractUser
from django.db import models
from catalogue.models import Entreprise  # à importer correctement selon ton arbo

class Utilisateur(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrateur'),
        ('RESP', 'Responsable stock'),
        ('MAG', 'Magasinier'),
        ('FOU', 'Fournisseur'),
    )
    role = models.CharField(max_length=10, choices=ROLES)
    entreprises = models.ManyToManyField(Entreprise)
    actif = models.BooleanField(default=True)
