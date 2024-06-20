from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListeDoc(models.Model):
    costumer = models.ForeignKey(User,on_delete=models.CASCADE)
    nom = models.TextField(max_length=32)
    prenom = models.TextField(max_length=32)
    specialite = models.TextField(max_length=32)
    exercice = models.TextField(max_length=32)
    ug = models.TextField(max_length=32)
    ville = models.TextField(max_length=32)
    adresse = models.TextField(max_length=132,null=True)
    potentiel = models.TextField(max_length=32)
    coeur_de_cibile = models.BooleanField()
    titre = models.TextField(max_length=32)
    frequence = models.IntegerField()
