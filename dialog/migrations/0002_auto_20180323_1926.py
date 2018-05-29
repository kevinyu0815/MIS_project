# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-03-23 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20)),
                ('response', models.CharField(max_length=100)),
                ('response_type', models.IntegerField(choices=[('1', 'TEXT'), ('2', 'CHOICE'), ('3', 'PICTURE')], default='1', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Management_interface',
        ),
    ]
