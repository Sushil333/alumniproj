# Generated by Django 4.0.4 on 2022-05-28 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_remove_career_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
