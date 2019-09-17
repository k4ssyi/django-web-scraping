from django.db import models
from django.utils import timezone


class Content(models.Model):
    """記事モデル."""
    class Meta(object):
        db_table = 'content'

    title = models.CharField(verbose_name='タイトル', max_length=255, unique=True)
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
