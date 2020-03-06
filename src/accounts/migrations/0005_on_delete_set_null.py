# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-12 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_typo_corrections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tutorial',
            field=models.ForeignKey(blank=True, help_text='The tutorial the student belongs to.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Tutorial'),
        ),
    ]
