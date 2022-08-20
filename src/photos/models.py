from django.db import models
from django.utils import timezone
from photo_gallery.models import Post

class Photo(models.Model):
    file = models.FileField(verbose_name='File', upload_to='media/', blank=False)
    uploaded_at = models.DateTimeField(verbose_name='Uploaded at', auto_now_add=timezone.now)

    def __str__(self) -> str:
        return f"Post {self.id} uploaded at {self.uploaded_at}"
