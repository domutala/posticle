from django.db import models
from django.contrib.auth.models import User

class Auteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length = 50)
    nom = models.CharField(max_length = 50)


    def __str__(self):
        return self.prenom + " " + self.nom

    class Meta:
        unique_together = ('user', 'prenom', 'nom')
        