# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_add_models'),
        ('items', '0001_add_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(related_name='location_of', to='transaction.Location'),
        ),
    ]
