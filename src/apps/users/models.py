from django.contrib.auth.models import User
from django.db import models
from os.path import join, basename
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from core.settings import BASE_DIR


# Create your models here.
class ExtendsUser(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER = (
        ('masculino','Masculino'),  
        ('feminino','Feminino'),
        ('nothing', 'Prefiro não dizer')
    )
    profile_background = models.ImageField(upload_to='user/background', default='default/background.jpg')
    profile_picture = models.ImageField(upload_to='user/profile', default='default/usuario.jpg')
    bio = models.TextField(max_length=500,
                           blank=True,)
    gender = models.CharField(max_length=20,
                              choices=GENDER,
                              default='nothing')


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ExtendsUser.objects.create(user=instance)
 

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.extendsuser.save()
        
    
    def picture_name(self):
        return basename(self.profile_picture.name)
    
    
    def background_name(self):
        return basename(self.profile_background.name)