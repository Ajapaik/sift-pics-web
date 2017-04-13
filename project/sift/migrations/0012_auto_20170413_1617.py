# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sift', '0011_auto_20151201_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catappliedtag',
            name='id',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
