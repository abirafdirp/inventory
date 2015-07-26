# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('sku', models.CharField(help_text=b'must be unique', unique=True, max_length=20, verbose_name=b'SKU')),
                ('product_id_prefix', models.CharField(help_text=b'must be unique, max length 7 characters', unique=True, max_length=7, verbose_name=b'Product ID prefix')),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'items', blank=True)),
                ('expires_in', models.IntegerField(help_text=b'this is NOT expiration date, but how long until this item will be expired in days. Leave blank if the item is not expireable', null=True, verbose_name=b'Expires in (days)', blank=True)),
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
                ('product_id', models.CharField(help_text=b'left blank to randomize based on product ID prefix', max_length=15, blank=True)),
                ('expiration_date', models.DateField()),
                ('expired', models.BooleanField(default=False)),
                ('base_item', models.ForeignKey(related_name='items', to='items.BaseItem')),
            ],
            options={
                'ordering': ('expiration_date',),
            },
        ),
    ]
