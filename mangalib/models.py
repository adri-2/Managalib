from django.db import models

# Create your models here.
class Auteur(models.Model):
    nom = models.CharField(max_length=64, unique = True)

class livre(models.Model):
    titre = models.CharField(max_length = 32, unique=True)
    quantity = models.IntegerField(default=1)
    auteur = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)

