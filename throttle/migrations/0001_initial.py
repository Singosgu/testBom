# Generated by Django 4.1.4 on 2023-03-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThrottleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, help_text='Is Delete', verbose_name='Is Delete')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='Update Time', null=True, verbose_name='Update Time')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='Create Time', null=True, verbose_name='Create Time')),
                ('ip', models.CharField(max_length=32, verbose_name='IP')),
                ('method', models.CharField(max_length=18, verbose_name='Method')),
                ('t_code', models.CharField(max_length=255, verbose_name='Transaction Code')),
            ],
            options={
                'verbose_name': 'bomiot Throttle',
                'verbose_name_plural': 'bomiot Throttle',
                'db_table': 'bomiot throttle',
                'ordering': ['-id'],
                'permissions': (),
            },
        ),
    ]
