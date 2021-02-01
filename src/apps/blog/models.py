from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    background = models.ImageField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=400)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    author_name = str(author)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)
    status = models.CharField(max_length=15,
                              choices=STATUS,
                              default='rascunho')
    class Meta():
        ordering = ('-published_at',)
    
    def __str__(self):
        return f'{self.title}|{str(self.author)}'