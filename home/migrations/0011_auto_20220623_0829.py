# Generated by Django 3.2.13 on 2022-06-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220622_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity_as_float',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
