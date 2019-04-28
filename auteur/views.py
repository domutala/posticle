from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Auteur
from .serializers import AuteurSerializer
from .permissions import IsOwnerOrReadOnly


class AuteurList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

    def get_queryset(self):
        self.queryset = Auteur.objects.all()
        return self.queryset


class AuteurDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

    def delete(self, request, *args, **kwargs):
        a = Auteur.objects.get(**kwargs)
        User.objects.filter(pk=a.user.id).delete()
        return self.destroy(request, *args, **kwargs)
