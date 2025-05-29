# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet

router = DefaultRouter()
router.register(r'api', UtilisateurViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]
