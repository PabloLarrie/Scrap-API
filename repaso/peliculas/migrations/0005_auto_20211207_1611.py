# Generated by Django 3.2.9 on 2021-12-07 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0004_rename_tittle_pelicula_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='rating',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='year',
            new_name='Year',
        ),
    ]