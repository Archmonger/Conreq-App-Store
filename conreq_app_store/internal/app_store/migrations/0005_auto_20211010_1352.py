# Generated by Django 3.2.7 on 2021-10-10 13:52

from django.db import migrations, models
import versionfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0004_auto_20211010_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apppackage',
            name='incompatible_apps',
        ),
        migrations.RemoveField(
            model_name='apppackage',
            name='optional_apps',
        ),
        migrations.RemoveField(
            model_name='apppackage',
            name='required_apps',
        ),
        migrations.AddField(
            model_name='apppackage',
            name='incompatible_app_packages',
            field=models.ManyToManyField(blank=True, related_name='_app_store_apppackage_incompatible_app_packages_+', to='app_store.AppPackage'),
        ),
        migrations.AddField(
            model_name='apppackage',
            name='optional_app_packages',
            field=models.ManyToManyField(blank=True, related_name='_app_store_apppackage_optional_app_packages_+', to='app_store.AppPackage'),
        ),
        migrations.AddField(
            model_name='apppackage',
            name='required_app_packages',
            field=models.ManyToManyField(blank=True, related_name='_app_store_apppackage_required_app_packages_+', to='app_store.AppPackage'),
        ),
        migrations.AlterField(
            model_name='apppackage',
            name='asynchronous',
            field=models.CharField(choices=[('NONE', 'No Async'), ('SEMI', 'Semi Async'), ('FULL', 'Fully Async')], default='NONE', max_length=20),
        ),
        migrations.AlterField(
            model_name='apppackage',
            name='minimum_conreq_version',
            field=versionfield.fields.VersionField(default='0.0.1'),
        ),
        migrations.AlterField(
            model_name='apppackage',
            name='tested_conreq_version',
            field=versionfield.fields.VersionField(default='1.0.0'),
        ),
        migrations.AlterField(
            model_name='apppackage',
            name='version',
            field=versionfield.fields.VersionField(default='0.0.1'),
        ),
    ]
