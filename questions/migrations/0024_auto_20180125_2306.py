# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0023_auto_20180125_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alternative',
            options={'ordering': ['title', 'created_at'], 'verbose_name': 'Alternative', 'verbose_name_plural': 'Alternatives'},
        ),
        migrations.RenameField(
            model_name='alternative',
            old_name='alternative_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Advanced', 'Advanced'), ('Intermediary', 'Intermediary'), ('Basic', 'Basic')], default='basic', help_text='Difficulty level', max_length=15, verbose_name='Level'),
        ),
    ]
