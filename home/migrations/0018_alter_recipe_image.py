# Generated by Django 3.2.13 on 2022-06-29 08:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20220628_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/samuel-dainton/image/upload/v1654348097/cld-sample-4.jpg', max_length=255, null=True, verbose_name='image'),
        ),
    ]
