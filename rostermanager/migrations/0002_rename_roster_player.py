# Generated by Django 4.1.7 on 2023-03-15 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rostermanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roster',
            new_name='Player',
        ),
    ]
