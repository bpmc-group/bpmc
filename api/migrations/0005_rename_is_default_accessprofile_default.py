# Generated by Django 5.1.3 on 2025-01-03 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_accessprofile_permission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessprofile',
            old_name='is_default',
            new_name='default',
        ),
    ]
