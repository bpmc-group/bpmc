# Generated by Django 5.1.3 on 2025-01-03 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_date_joined_user_groups_user_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_name', models.CharField(max_length=255)),
                ('can_add', models.BooleanField(default=False)),
                ('can_edit', models.BooleanField(default=False)),
                ('can_delete', models.BooleanField(default=False)),
                ('can_view', models.BooleanField(default=False)),
                ('access_scope', models.CharField(choices=[('Various', 'Various'), ('Allowed', 'Allowed')], default='Various', max_length=255)),
                ('access_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='api.accessprofile')),
            ],
        ),
    ]
