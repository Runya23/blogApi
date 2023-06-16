from django.db import models

from django.db import models
from posts.models import Post


class Like(models.Model):
    owner = models.ForeignKey('auth.User', related_name= 'likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name= 'likes', on_delete=models.CASCADE)


    class Meta:
        unique_together = ['owner', 'post']

class Favorite(models.Model):
    owner = models.ForeignKey('auth.User', related_name= 'favorites', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name= 'favorites', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'post']

