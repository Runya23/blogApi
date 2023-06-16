from rest_framework import serializers
from .models import Comment


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Comment
        fields = '_all__'