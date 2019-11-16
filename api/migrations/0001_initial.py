# Generated by Django 2.2.4 on 2019-08-20 03:23

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(editable=False, max_length=15, unique=True)),
                ('tasks', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('content_data', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('uuid', models.CharField(editable=False, help_text="Log's UUID.", max_length=22, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Log creation date.')),
                ('expires', models.DateTimeField(help_text='Log expiration date.', null=True)),
                ('content', models.TextField(editable=False, help_text='Raw log content.')),
                ('type', models.CharField(help_text='Log type.', max_length=30, null=True)),
                ('users', django.contrib.postgres.fields.jsonb.JSONField(default=list, help_text='List of users in log.')),
                ('owner', models.ForeignKey(help_text='Log owner.', on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'permissions': [('extended_expiry', 'Can set an expiry time of up to two weeks'), ('no_expiry', 'Can set an infinite expiry time, or none at all')],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', django.contrib.postgres.fields.jsonb.JSONField(editable=False, help_text="Page's users.")),
                ('messages', django.contrib.postgres.fields.jsonb.JSONField(editable=False, help_text="Page's messages.")),
                ('index', models.IntegerField(editable=False, help_text='Page index.')),
                ('log', models.ForeignKey(editable=False, help_text='Log', on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='api.Log')),
            ],
        ),
    ]
