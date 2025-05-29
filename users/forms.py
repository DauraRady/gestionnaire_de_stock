from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class RegisterForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'role', 'entreprises', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['entreprises'].widget = forms.CheckboxSelectMultiple()
