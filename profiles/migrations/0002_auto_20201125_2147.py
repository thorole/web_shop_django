# Generated by Django 3.1.2 on 2020-11-25 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_True',
            new_name='default_town_or_city',
        ),
    ]
