# Generated by Django 4.1.4 on 2023-04-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_error_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time'),
        ),
    ]
