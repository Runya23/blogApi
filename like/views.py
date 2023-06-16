from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Like
from . import serializers 
from posts.permissions import IsAuthor

class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    serializer_class = serializers.LikeSerializers

    def perform_create(self, serializer):
        serializers.save(owner=self.request.user)

class LikeDeleteView(generics.DestroyAPIView):
    queryset= Like.objects.all()
    permission_classes = (IsAuthor)
