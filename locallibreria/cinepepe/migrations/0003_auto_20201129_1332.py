# Generated by Django 3.0.5 on 2020-11-29 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinepepe', '0002_auto_20201129_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Director', 'verbose_name_plural': 'Directores'},
        ),
        migrations.AlterModelTable(
            name='director',
            table='directores',
        ),
    ]
