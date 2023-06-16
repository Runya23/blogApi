from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    owner  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.owner} -> {self.body}"