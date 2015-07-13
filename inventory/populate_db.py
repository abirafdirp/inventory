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
from transaction.models import Location
from transaction.models import Transaction
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
    Item.objects.all().delete()
    Location.objects.all().delete()
    print 'current database cleared'

    add_baseitem(owner=owner, name='Galaxy S6', sku='SMSNGGLXY6',
                 brand='Samsung', product_id_prefix='GLXY6A',
                 category='Smartphone', expires_in=0)
    add_baseitem(owner=owner, name='Galaxy S6 Edge', sku='SMSNGGLXY6E',
                 brand='Samsung', product_id_prefix='GLXY6E',
                 category='Smartphone', expires_in=0)
    add_baseitem(owner=owner, name='Galaxy S5', sku='SMSNGGLXY5',
                 brand='Samsung', product_id_prefix='GLXY5A',
                 category='Smartphone', expires_in=0)
    add_location(owner=owner, name='Jakarta', address='Pondok Labu',
                 type='Warehouse')
    add_location(owner=owner, name='Bogor', address='Kebun raya',
                 type='Store')
    for a in range(5):
        add_item(owner=owner, base_item='Galaxy S5', location='Jakarta')
        add_item(owner=owner, base_item='Galaxy S6', location='Jakarta')
        add_item(owner=owner, base_item='Galaxy S6 Edge', location='Jakarta')


def add_location(owner, name, type, address):
    # Type field are choices, this is the validation
    try:
        location, created = Location.objects.get_or_create\
            (owner=owner, name=name, type=type, address=address)
        display(name+' '+type, 'location')
        return location
    except:
        print """Wrong type. Avaiable types are (Warehouse, Store'+
              , Refurbish/Recycling Center/Landfill, Supplier"""
        return


def add_item(owner, location, base_item, product_id=''):

    # because creating base item through item will be too much,
    # there will be get_or_create method
    try:
        base_item = BaseItem.objects.get(name=base_item)
    except:
        print 'Base item %s does not exist. Please create it first' \
              %(base_item)
        return

    try:
        location = Location.objects.get(name=location)
    except DoesNotExist:
        print 'Location %s does not exist. Please create it first' \
              %(base_item)
        return
    item, created = Item.objects.get_or_create\
        (owner=owner, base_item=base_item, location=location,
         product_id=product_id)
    item.save()
    display(base_item, 'item')
    return item


def add_baseitem(owner, name, sku, brand, category, product_id_prefix,
                 expires_in, description='', image=''):

    # using get_or_create will return a tuple, that is the instance and
    # the boolean if the object already exist or not. manytomany field must
    # added through add function
    brand, created = Brand.objects.get_or_create(owner=owner, name=brand)
    category, created = Category.objects.get_or_create(owner=owner,
                                                       name=category)
    product_id_prefix, created = ProductIdPrefix.objects.get_or_create\
        (owner=owner, name=product_id_prefix)

    base_item, created = BaseItem.objects.get_or_create\
        (owner=owner, name=name, sku=sku, description=description, brand=brand,
         product_id_prefix=product_id_prefix, image=image,
         expires_in=expires_in)
    base_item.category.add(category)
    display(name, 'base item')
    return base_item


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




