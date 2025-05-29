from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

from rest_framework import viewsets
from .models import Utilisateur
from .serializers import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


