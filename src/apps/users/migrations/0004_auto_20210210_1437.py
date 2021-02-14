# Generated by Django 3.1.5 on 2021-02-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210210_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendsuser',
            name='nickname',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001AF046CB370>', max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='extendsuser',
            name='profile_background',
            field=models.ImageField(default='../../public/static/img/background.jpg', upload_to='../../data/media'),
        ),
        migrations.AlterField(
            model_name='extendsuser',
            name='profile_picture',
            field=models.ImageField(default='../../public/static/img/background.jpg', upload_to='../../data/media'),
        ),
    ]
