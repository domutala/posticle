from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import permissions

from auteur.permissions import IsOwnerOrReadOnly, IsAuthorOrReadOnly
from auteur.models import Auteur
from .models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        auteur = Auteur.objects.get(user=self.request.user)
        serializer.save(auteur=auteur)
        # return super().perform_create(serializer)

    def get_queryset(self):
        self.queryset = Article.objects.all()
        return self.queryset

class ArticleListByAuteur(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    serializer_class = ArticleSerializer

    def get_queryset(self):
        self.auteur = get_object_or_404(Auteur, id=self.kwargs['auteur_id'])
        self.queryset = Article.objects.filter(auteur=self.auteur)
        return self.queryset


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
