# Generated by Django 4.1.7 on 2023-03-15 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('player_num', models.PositiveIntegerField()),
                ('position', models.CharField(choices=[('C', 'Center'), ('LW', 'Left Wing'), ('RW', 'Right Wing'), ('LD', 'Left Defense'), ('RD', 'Right Defense'), ('G', 'Goalie')], max_length=2)),
                ('on_roster', models.BooleanField(default=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rostermanager.season')),
            ],
        ),
    ]
