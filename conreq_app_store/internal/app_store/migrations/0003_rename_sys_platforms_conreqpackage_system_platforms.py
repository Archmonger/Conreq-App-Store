# Generated by Django 3.2.7 on 2021-10-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0002_auto_20211010_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conreqpackage',
            old_name='sys_platforms',
            new_name='system_platforms',
        ),
    ]
