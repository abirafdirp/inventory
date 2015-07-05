# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_fix_location_representational_and_change_expires_on_to_datefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='expireable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='expires_on',
            field=models.DateField(null=True, blank=True),
        ),
    ]
