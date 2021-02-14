from django.contrib.auth.models import User
from django.db import models
from os.path import join

# Create your models here.
class ExtendsUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    GENDER = (
        ('masculino','Masculino'),  
        ('feminino','Feminino'),
        ('nothing', 'Prefiro não dizer')
    )
    profile_background = models.ImageField(upload_to='../../data/media', default='../../public/static/img/background.jpg')
    profile_picture = models.ImageField(upload_to='../../data/media', default='../../public/static/img/background.jpg')
    nickname = models.CharField(max_length=40,
                                unique=True,
                                default=str(User.username))
    bio = models.TextField(max_length=500,
                           blank=True,)
    gender = models.CharField(max_length=20,
                              choices=GENDER,
                              default='nothing')