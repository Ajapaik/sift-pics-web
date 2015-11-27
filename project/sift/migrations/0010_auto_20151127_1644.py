# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sift', '0009_catphoto_date_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catphoto',
            name='title',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
