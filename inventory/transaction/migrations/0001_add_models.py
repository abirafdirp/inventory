# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_add_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=15, choices=[(b'warehouse', b'warehouse'), (b'store', b'store')])),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('items_in', models.IntegerField(null=True, blank=True)),
                ('items_out', models.IntegerField(null=True, blank=True)),
                ('destination', models.ForeignKey(related_name='destination_of', blank=True, to='transaction.Location', null=True)),
                ('items', models.ManyToManyField(to='items.Item')),
                ('origin', models.ForeignKey(related_name='origin_of', blank=True, to='transaction.Location', null=True)),
            ],
        ),
    ]
