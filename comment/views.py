from django.shortcuts import render
from rest_framework import generics, permissions
from posts.permissions import IsAuthorOrAdminPostOwner
from .models import Comment
from . import serializers


class CommentCreateView(generics.CreateAPIView):
    serializers_class = serializers.CommentSerializers
    permissions_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializers):
        serializers.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset= Comment.objects.all()
    serializer_class= serializers.CommentSerializers

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsAuthorOrAdminPostOwner()