from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from core.settings import BASE_DIR
from os.path import join


class post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    background = models.ImageField()
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=400)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    author_name = str(author)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.CharField(max_length=15,
                              choices=STATUS,
                              default='rascunho')
    
    class Meta():
        ordering = ('-published_at',)
    
    def __str__(self):
        return f'{self.title}|{str(self.author)}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_blog', kwargs={'slug':self.slug})

    def get_absolute_url_to_delete(self):
        return reverse('delete_post', kwargs={'slug':self.slug})

    def get_absolute_url_to_edit(self):
        return reverse('edit_post', kwargs={'slug':self.slug})