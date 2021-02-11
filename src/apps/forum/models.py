from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class question(models.Model):
    STATUS = (
        ('em aberto','Em Aberto'),
        ('resolvido','Resolvido'),
    )
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    author_name = str(author)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)
    status = models.CharField(max_length=15,
                              choices=STATUS,
                              default='em aberto')
    class Meta():
        ordering = ('-created_at',)
    
    def __str__(self):
        return f'{self.title}|{str(self.author)}'