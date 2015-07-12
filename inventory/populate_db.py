import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'config.settings.local')

import sys
import django
django.setup()

from items.models import BaseItem
from items.models import Item
from items.models import Brand
from items.models import ProductIdPrefix
from items.models import Category
from inventory.users.models import User

def populate():

    # get user for auth, username is from command line argument
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    print username
    try:
        owner = User.objects.get(username=username, password=password)
    except:
        print 'invalid username or password
        return
    # add_category()

def add_page(cat, title, url, views=0):
    p = BaseItem.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_category(owner, name):
    c = Category.objects.get_or_create(owner=owner, name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()




