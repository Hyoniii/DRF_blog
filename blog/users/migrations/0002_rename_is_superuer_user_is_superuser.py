# Generated by Django 3.2.9 on 2021-11-29 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_superuer',
            new_name='is_superuser',
        ),
    ]