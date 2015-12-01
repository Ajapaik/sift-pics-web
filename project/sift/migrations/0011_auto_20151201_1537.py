# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sift', '0010_auto_20151127_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalbum',
            name='subtitle_sv',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='catalbum',
            name='title_sv',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
