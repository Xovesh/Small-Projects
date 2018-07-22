# Generated by Django 2.0.5 on 2018-07-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0002_auto_20180722_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='abilities',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='category',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='firstevolution',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='gender',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='ptype',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='special_attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='special_defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weakness',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
