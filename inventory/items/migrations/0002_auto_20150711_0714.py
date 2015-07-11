# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(related_name='location_of', to='transaction.Location'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(related_name='items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='brand',
            name='owner',
            field=models.ForeignKey(related_name='brands', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='baseitem',
            name='brand',
            field=models.ForeignKey(related_name='brand_of', to='items.Brand'),
        ),
        migrations.AddField(
            model_name='baseitem',
            name='category',
            field=models.ManyToManyField(related_name='category_of', to='items.Category'),
        ),
        migrations.AddField(
            model_name='baseitem',
            name='owner',
            field=models.ForeignKey(related_name='base_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='baseitem',
            name='product_id_prefix',
            field=models.OneToOneField(null=True, to='items.ProductIdPrefix', blank=True, help_text=b'must be unique', verbose_name=b'Product ID prefix'),
        ),
    ]
