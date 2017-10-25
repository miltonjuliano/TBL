# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 00:00
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
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Discipline title', max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Discipline description', verbose_name='Description')),
                ('course', models.CharField(blank=True, help_text='Discipline course', max_length=100, verbose_name='Course')),
                ('slug', models.SlugField(verbose_name='Shortcut')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date that the discipline is created.', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date that the discipline is updated.', verbose_name='Updated at')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplines', to=settings.AUTH_USER_MODEL, verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Discipline',
                'ordering': ['title', 'created_at'],
                'verbose_name_plural': 'Disciplines',
            },
        ),
    ]