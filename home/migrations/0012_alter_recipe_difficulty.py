# Generated by Django 3.2.13 on 2022-06-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_recipe_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('advanced', 'Advanced')], default='Easy', max_length=50),
        ),
    ]
