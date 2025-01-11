from django.db import models

# Create your models here.
class Auteur(models.Model):
    nom = models.CharField(max_length=64, unique = True,verbose_name="Nom")
    class Meta:
        verbose_name ="Auteur"
        verbose_name_plural ="Auteurs"
    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length = 32, unique=True,verbose_name="Titre")
    quantity = models.IntegerField(default=1,verbose_name="Quantité")
    auteur = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING,verbose_name="Auteur")
    #date = models.DateField(verbose_name="Date de diffusion")
    class Meta:
        verbose_name ="Livre"
        verbose_name_plural ="Livres"
    def __str__(self):
        return self.titre

