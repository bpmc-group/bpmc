# Generated by Django 5.1.3 on 2025-01-04 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        ('api', '0008_alter_user_access_profiles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccessProfile',
        ),
    ]
