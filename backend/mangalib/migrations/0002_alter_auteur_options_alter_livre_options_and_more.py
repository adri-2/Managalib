# Generated by Django 5.0.2 on 2024-02-29 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auteur',
            options={'verbose_name': 'Auteur', 'verbose_name_plural': 'Auteurs'},
        ),
        migrations.AlterModelOptions(
            name='livre',
            options={'verbose_name': 'Livre', 'verbose_name_plural': 'Livres'},
        ),
        migrations.AlterField(
            model_name='auteur',
            name='nom',
            field=models.CharField(max_length=64, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mangalib.auteur', verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantité'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='titre',
            field=models.CharField(max_length=32, unique=True, verbose_name='Titre'),
        ),
    ]
