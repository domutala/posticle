from rest_framework import serializers
from django.contrib.auth.models import User
from user.serializers import UserSerializer
from .models import Article

class ArticleSerializer(serializers.Serializer):
    auteur = serializers.ReadOnlyField(source="auteur.prenom")
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()


    def create(self, validated_data):
        # Create and return a new 'Article' instance, given the validated data.
        article = Article.objects.create(**validated_data)
        return article
       
    def update(self, instance, validated_data):
        # Update and return an existing 'Article' instance, given the validated data.
        
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = ('user', 'id', 'title', 'content')
