# Generated by Django 3.0 on 2021-08-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='puntaje',
            field=models.IntegerField(default=0),
        ),
    ]
