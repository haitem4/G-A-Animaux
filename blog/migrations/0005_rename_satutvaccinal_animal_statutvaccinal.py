# Generated by Django 4.0.4 on 2022-06-22 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_animal_categorie_delete_catanimal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='SatutVaccinal',
            new_name='StatutVaccinal',
        ),
    ]
