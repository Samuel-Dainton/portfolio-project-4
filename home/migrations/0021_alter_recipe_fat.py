# Generated by Django 3.2.13 on 2022-06-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_recipe_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='fat',
            field=models.CharField(blank=True, default='Unspecified', max_length=50, null=True),
        ),
    ]
