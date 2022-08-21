from django.db import models
from django.utils import timezone
from authentication.models import User

class Post(models.Model):
    file = models.ForeignKey('photos.Photo', verbose_name='File', related_name="post_file", on_delete=models.PROTECT, blank=False)
    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.PROTECT, blank=False)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    comments = models.ManyToManyField(User, related_name="commented_posts", through="Comment")
    is_approved = models.BooleanField(verbose_name='Is approved', default=False)
    created_at = models.DateTimeField(verbose_name='Uploaded at', auto_now_add=timezone.now)

    def __str__(self) -> str:
        return f'Uploaded by {self.owner} at {self.created_at}'


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.PROTECT, blank=False)
    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE, blank=False)
    text = models.CharField(verbose_name='Comment text', max_length=200, null=False, blank=False)
    created = models.DateTimeField(verbose_name='Created at', auto_now_add=timezone.now)

    def __str__(self) -> str:
        return self.text