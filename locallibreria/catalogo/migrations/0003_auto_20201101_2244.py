# Generated by Django 3.1.2 on 2020-11-02 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_movieinstance_release_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieinstance',
            options={'ordering': ['release_date']},
        ),
        migrations.RemoveField(
            model_name='movieinstance',
            name='due_back',
        ),
    ]