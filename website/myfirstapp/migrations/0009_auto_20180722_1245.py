# Generated by Django 2.0.5 on 2018-07-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0008_auto_20180722_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='gender',
            field=models.IntegerField(),
        ),
    ]
