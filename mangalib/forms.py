from django import forms
from .models import Auteur, livre

"""
class SomeFrom(forms.Form):
    username = forms.CharField(label="Nom utilisateur")
    password = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput)
    langages = [('c','langage c'),('p','langage python'),('h','langage html')]
    langage = forms.MultipleChoiceField(label="Programme",widget=forms.CheckboxSelectMultiple,
                                        choices=langages)
"""
class LivreForm(forms.ModelForm):
    auteur = forms.ModelChoiceField(queryset= Auteur.objects.all(),label="Auteur")
    class Meta:
        model = livre
        fields = ['titre','quantity','auteur']
        labels = {'titre':'Titre','quantity':'Quantité'}
    
    
       
