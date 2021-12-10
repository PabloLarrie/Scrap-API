# Generated by Django 3.2.9 on 2021-12-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_auto_20211206_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
