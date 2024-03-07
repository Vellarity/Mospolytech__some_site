# Generated by Django 5.0.2 on 2024-03-07 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_bio_profile_fio_profile_email_profile_geo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wearcomment',
            old_name='wear_id',
            new_name='wear',
        ),
        migrations.RemoveField(
            model_name='wearcomment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='wearcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.profile'),
        ),
    ]