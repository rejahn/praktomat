# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-04 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0009_isabelle_checker_trusted_to_additional_theories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isabellechecker',
            name='additional_theories',
            field=models.CharField(blank=True, help_text='Isabelle theories to be run in addition to those provided by the user (Library theories or theories uploaded using the Create File Checker). Do not include the file extensions. Separate multiple theories by space', max_length=200),
        ),
    ]
