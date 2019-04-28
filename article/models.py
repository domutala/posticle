from django.db import models
from auteur.models import Auteur

class Article(models.Model):
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
