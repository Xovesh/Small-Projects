# Generated by Django 2.0.5 on 2018-05-31 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='genre',
            new_name='gender',
        ),
    ]
