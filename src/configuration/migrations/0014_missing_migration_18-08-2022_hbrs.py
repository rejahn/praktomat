# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-18 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0013_settings_tutors_can_edit_solutions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='accept_all_solutions',
            field=models.BooleanField(default=False, help_text='If enabled, solutions can become the final solution even if not all required checkers are passed.'),
        ),
    ]