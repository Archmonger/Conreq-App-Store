# Generated by Django 3.2.7 on 2021-10-10 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0008_auto_20211010_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='environmentvariable',
            old_name='example',
            new_name='example_values',
        ),
    ]
