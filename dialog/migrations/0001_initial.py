# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-03-20 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.BooleanField(default=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(default=' ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Management_interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=50)),
                ('reply', models.TextField(max_length=50)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=2)),
                ('email', models.EmailField(default=' ', max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='dialog',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dialog.Member'),
        ),
    ]
