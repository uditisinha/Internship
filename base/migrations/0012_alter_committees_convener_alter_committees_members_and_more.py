# Generated by Django 5.0 on 2023-12-25 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_committees_convener_alter_committees_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committees',
            name='convener',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='committees',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='committees',
            name='staff',
            field=models.ManyToManyField(blank=True, null=True, related_name='staff', to=settings.AUTH_USER_MODEL),
        ),
    ]
