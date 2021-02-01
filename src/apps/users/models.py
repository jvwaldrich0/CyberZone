from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ExtendsUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    GENDER = (
        ('masculino','Masculino'),
        ('feminino','Feminino'),
        ('nothing', 'Prefiro não dizer')
    )
    profile_background = models.ImageField()
    profile_picture = models.ImageField()
    nickname = models.CharField(max_length=40,
                                unique=True,
                                primary_key=True)
    bio = models.TextField(max_length=500,
                           blank=True)
    gender = models.CharField(max_length=20,
                              choices=GENDER,
                              default='nothing')
    