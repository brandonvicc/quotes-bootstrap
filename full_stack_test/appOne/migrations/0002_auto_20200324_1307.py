# Generated by Django 2.2 on 2020-03-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='author',
            new_name='author_by',
        ),
    ]
