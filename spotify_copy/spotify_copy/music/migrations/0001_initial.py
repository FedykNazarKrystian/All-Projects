# Generated by Django 5.1 on 2024-08-18 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='songs/')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song')),
            ],
        ),
    ]
