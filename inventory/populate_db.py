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

    smartphone = add_category(owner=owner, name='Smartphone')

    samsung = add_brand(owner=owner, name='Samsung')

    glxy6prefix = add_productidprefix(owner=owner, name='SMGG6-')

    glxy6base = add_baseitem(owner=owner, name='Galaxy S6', sku='SMSNGGLXY6',
                             brand=samsung, product_id_prefix=glxy6prefix,
                             category=smartphone, expires_in=0)

# def additem()

def add_baseitem(owner, name, sku, brand, category, product_id_prefix,
                 expires_in, description='', image=''):
    b = BaseItem.objects.get_or_create\
        (owner=owner, name=name, sku=sku, brand=brand, category=category,
         product_id_prefix=product_id_prefix, description=description,
         image=image, expires_in=expires_in)
    display(name, 'base item')
    return b

def add_productidprefix(owner, name):
    b = ProductIdPrefix.objects.get_or_create(owner=owner, name=name)[0]
    b.save()
    display(name, 'product ID prefix')
    return b

def add_brand(owner, name):
    b = Brand.objects.get_or_create(owner=owner, name=name)[0]
    b.save()
    display(name, 'brand')
    return b

def add_category(owner, name):
    c = Category.objects.get_or_create(owner=owner, name=name)[0]
    b.save()
    display(name, 'category')
    return c

def display(name, model):
    print 'Added %s in %s' %(name, model)

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()




