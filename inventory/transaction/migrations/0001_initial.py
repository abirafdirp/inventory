# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=35, choices=[(b'Warehouse', b'Warehouse'), (b'Store', b'Store'), (b'Refurbish/Recycling Center/Landfill', b'Refurbish/Landfill/Recyling center'), (b'supplier', b'Supplier')])),
                ('address', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('items_count', models.IntegerField(null=True, blank=True)),
                ('destination', models.ForeignKey(related_name='destinations', to='transaction.Location')),
                ('item', models.ForeignKey(related_name='transactions', to='items.BaseItem')),
                ('origin', models.ForeignKey(related_name='origins', to='transaction.Location')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_time',),
            },
        ),
    ]
