from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from . import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """creating new recipe"""
        serializer.save(user=self.request.user)
