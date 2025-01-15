# Generated by Django 5.1.3 on 2025-01-03 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        ('api', '0006_alter_permission_function_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_profiles',
            field=models.ManyToManyField(blank=True, related_name='users', to='administration.accessprofile'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='function_name',
            field=models.CharField(max_length=255),
        ),
    ]
