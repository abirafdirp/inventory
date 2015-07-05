# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_modify_category_plural_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expires_on',
            field=models.DateField(default=datetime.date(2099, 12, 12)),
        ),
    ]
