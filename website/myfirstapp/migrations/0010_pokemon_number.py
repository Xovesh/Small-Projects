# Generated by Django 2.0.5 on 2018-07-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0009_auto_20180722_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='number',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
