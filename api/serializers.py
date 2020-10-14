from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Movie, Rating

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User object """
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    """ Serializer for Movie object """
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_ratings']


class RatingSerializer(serializers.ModelSerializer):
    """ Serializer for Rating object """
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'user', 'stars']
