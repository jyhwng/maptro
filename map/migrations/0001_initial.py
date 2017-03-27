# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, verbose_name='How would you call this station?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('matrix', models.CharField(max_length=30)),
                ('text_anchor', models.CharField(max_length=10)),
                ('line', models.ManyToManyField(to='map.Line')),
            ],
        ),
        migrations.AddField(
            model_name='nick',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Station'),
        ),
        migrations.AddField(
            model_name='like',
            name='nick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Nick'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
