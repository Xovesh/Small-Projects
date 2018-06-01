# Generated by Django 2.0.5 on 2018-05-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('height', models.FloatField()),
                ('weigth', models.FloatField()),
                ('genre', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=200)),
                ('abilities', models.CharField(max_length=200)),
                ('ptype', models.CharField(max_length=200)),
                ('weakness', models.CharField(max_length=200)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('firstevolution', models.BooleanField()),
            ],
        ),
    ]
