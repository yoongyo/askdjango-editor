# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180612_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
