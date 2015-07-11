# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('sku', models.CharField(unique=True, max_length=20, verbose_name=b'SKU')),
                ('description', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(upload_to=b'items', blank=True)),
                ('expires_in', models.IntegerField(help_text=b'This is NOT expiration date, but how long until this item will be expired in days. Leave blank if the item is not expireable', null=True, verbose_name=b'Expires in (days)', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.CharField(help_text=b'Product ID will be generatedrandomly to simulate shipment from supplier', max_length=15, blank=True)),
                ('expiration_date', models.DateField()),
                ('expired', models.BooleanField(default=False)),
                ('base_item', models.ForeignKey(related_name='base_item_of', to='items.BaseItem')),
            ],
            options={
                'ordering': ('expiration_date',),
            },
        ),
        migrations.CreateModel(
            name='ProductIdPrefix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Max length 7 characters', unique=True, max_length=7)),
                ('owner', models.ForeignKey(related_name='product_id_prefixes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Product ID Prefixes',
            },
        ),
    ]
