# Generated by Django 3.2.7 on 2021-10-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0003_alter_apppackage_license_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apppackage',
            name='description',
        ),
        migrations.AddField(
            model_name='apppackage',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apppackage',
            name='development_stage',
            field=models.CharField(choices=[('1 - Planning', 'Planning'), ('2 - Pre-Alpha', 'Pre-Alpha'), ('3 - Alpha', 'Alpha'), ('4 - Beta', 'Beta'), ('5 - Production/Stable', 'Stable'), ('6 - Mature', 'Mature'), ('7 - Inactive', 'Inactive')], default='2 - Pre-Alpha', max_length=21),
        ),
    ]
