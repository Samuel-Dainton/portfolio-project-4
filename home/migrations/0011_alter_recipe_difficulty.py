# Generated by Django 3.2.13 on 2022-06-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220627_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'EASY'), ('moderate', 'MODERATE'), ('advanced', 'ADVANCED')], default='Easy', max_length=50),
        ),
    ]
