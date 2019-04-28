from rest_framework import serializers
from django.contrib.auth.models import User
from user.serializers import UserSerializer
from .models import Auteur

class AuteurSerializer(serializers.Serializer):
    user = UserSerializer()
    prenom = serializers.CharField(max_length = 50)
    nom = serializers.CharField(max_length = 50)


    def create(self, validated_data):
        # Create and return a new `Snippet` instance, given the validated data.

        user_data = validated_data.pop('user')
        user_data.pop('groups')
        user = User.objects.create_user(**user_data)

        auteur = Auteur.objects.create(user=user, **validated_data)
        return auteur
       
    def update(self, instance, validated_data):
        # Update and return an existing `Snippet` instance, given the validated data.
        
        instance.prenom = validated_data.get('prenom', instance.prenom)
        instance.nom = validated_data.get('nom', instance.nom)
        
        instance.save()
        return instance

    class Meta:
        model = Auteur
        fields = ('user', 'id', 'prenom', 'nom')
