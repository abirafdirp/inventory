import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'config.settings.local')

import sys
import django
django.setup()

from django.conf import settings
from django.contrib.auth.models import check_password
from django.contrib.auth import authenticate
from items.models import BaseItem
from items.models import Item
from items.models import Brand
from items.models import ProductIdPrefix
from items.models import Category
from inventory.users.models import User

def populate():

    # get user for auth, username is from command line argument
    username = str(sys.argv[1])
    try:
        owner = User.objects.get(username=username)
    except:
        print 'invalid username or password'
        return

    # clear current database
    BaseItem.objects.all().delete()
    print 'current database cleared'

    glxy6base = add_baseitem(owner=owner, name='Galaxy S6', sku='SMSNGGLXY6',
                             brand='Samsung', product_id_prefix='GLXY6A',
                             category='Smartphone', expires_in=0)

# def additem()

def add_baseitem(owner, name, sku, brand, category, product_id_prefix,
                 expires_in, description='', image=''):
    b = BaseItem.objects.create\
        (owner=owner, name=name, sku=sku, description=description,
         image=image, expires_in=expires_in)
    b.save()

    try:
        b.category.create(owner=owner, name=category)
    except:
        c = Category.objects.get(name=category)
        b.category.add(c)

    try:
        b.brand.create(owner=owner, name=brand)
    except:
        b.brand.add(Brand.objects.get(name=brand))
    try:
        b.product_id_prefix.create(owner=owner, name=product_id_prefix)
    except:
        b.product_id_prefix.create(ProductIdPrefix.objects.get\
            (name=product_id_prefix))



    # b.brand.get_or_create(owner=owner, name=brand)
    # b.product_id_prefix.get_or_create(owner=owner, name=product_id_prefix)
    display(name, 'base item')
    return b


def add_productidprefix(owner, name):
    b = ProductIdPrefix.objects.get_or_create(owner=owner, name=name)[0]
    display(name, 'product ID prefix')
    return b


def add_brand(owner, name):
    b = Brand.objects.get_or_create(owner=owner, name=name)[0]
    display(name, 'brand')
    return b


def add_category(owner, name):
    c = Category.objects.get_or_create(owner=owner, name=name)[0]
    display(name, 'category')
    return c


def display(name, model):
    print 'Added %s in %s' %(name, model)

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()




