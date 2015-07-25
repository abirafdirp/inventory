import json
from django import template
from items.models import Item
from items.models import BaseItem
from transaction.models import Transaction
from transaction.models import Location

register = template.Library()


class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

@register.assignment_tag
def get_items_in_locations():
    items_in_a_location = AutoVivification()
    counter = 0
    counteritems = 0
    lastlocation = ''
    lastitem = ''
    items = Item.objects.all()
    for item in items:
        if str(item.location) != lastlocation:
            counter += 1
            counteritems = 0
        if str(item.base_item.name) != lastitem:
            items_in_a_location[counter]['name'] = str(item.base_item.name)
        items_in_a_location[counter]['location'] = str(item.location)
        items_in_a_location[counter]['count'] = counteritems
        lastlocation = str(item.location)
        lastitem = str(item.base_item.name)
        counteritems += 1
    return json.JSONEncoder().encode(items_in_a_location)

for location in Location.objects.all():
    for item in location.items.all():
        pass





